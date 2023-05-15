from fastapi import APIRouter, Depends,HTTPException, status,Response,Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ...utils import database
from ..crud import token,oauth2,emails
from .. import schema
import uuid
from ..hashing import Hash






router = APIRouter()

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/login')
def login(response: Response,request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    return token.user_login(response,request,db)

@router.post("/forgot_password")
def forgot_password(request: schema.ForgotPassword, db: database.SessionLocal = Depends(database.get_db)):
    # check user exised
    result = oauth2.find_exit_user(request.email,db)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create reset code and save in database
    reset_code = str(uuid.uuid1())
    oauth2.create_reset_code(request.email,reset_code,db)
    # Sending email
    subject = "Hello"
    recipient = [request.email]
    messages ="""
  <!DOCTYPE html>
    <html>
        <head>
            <title>Reset password</title>
        </head>
        <body>
            <div class="contener" style=" background: rgb(95, 221, 252);
            width: 80%;
            margin: auto;
            padding: 1rem;">
                <h4>Hello, {0}</h4>
                <p>
                    Someone have request a link reset your password. If you requested this,your code is <b> {1}</b> and
                    you can change your password through the button 
                    <br><button style="background: rgb(235, 176, 27);
                    border: none;
                    padding: 5px 10px;"><a href="http://127.0.0.1:8000/docs#/Authentication/forgot_password_forgot_password_post?reset_password_token={1}" style="box-sizing: border-box ; border-color:red;">Reset Password</a></button>
                </p>
                <p>If you didn't request this, you can ignore this email</p>
                <p>Your password won't change until you access the link above and create a new one <br>Thank you</p>
            </div>
        </body>
    </html>
    """.format(request.email,reset_code)
    emails.send_mail(subject,recipient,messages)
    
    return {
        "reset_code":reset_code,
        "code":200,
        "message":"We are sent an email with instructions to reset your password"
    }
    
@router.post("/logout")
def logout(request:Request,token:str= Depends(oauth2.get_token_user), db: database.SessionLocal = Depends(database.get_db)):
    current_user = request.cookies.get('username')
    oauth2.save_black_list_token(token,db,current_user)
    return {"status_code": status.HTTP_200_OK,"detail":"Logged out successfully"}
    
    
@router.post("/reset_password") 
def reset_password(request:schema.ResetPassword,db: database.SessionLocal = Depends(database.get_db)):
    # check valid reset password token
    reset_token = oauth2.check_reset_password_token(request.reset_password_token,db)
    if not reset_token:
        raise HTTPException(status_code=404,detail="Reset password token have expired, please request a new one.")
    
    # check both new & confirm password are matched
    if request.new_password != request.confirm_password:
         raise HTTPException(status_code=404,detail="New password is not matched")

    # reset new password 
    forgot_password_object = reset_token.email
    new_hashed_password =  Hash.bcrypt(request.new_password)
    oauth2.reset_password(new_hashed_password, forgot_password_object,db)

    # Disable reset password code(alredy used)
    oauth2.disable_reset_code(request.reset_password_token,forgot_password_object,db)

    return {
        "code":200,
        "message":"Password has been reset successfully"
    }