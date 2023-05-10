# Auth-fastAPI
- create venv
python3 -m venv fastapi-env
- activate venv
source fastapi-env/bin/activate
- install fastapi
pip3 install fastapi
- install uvicorn in venv
pip3 install uvicorn



+ use docker and psql in fastapi
- pull postgres:alpine
docker pull postgres:alpine 
- check docker images
docker images
- create docker container
docker run --name fastapi-auth -e POSTGRES_PASSWORD=password -d -p 5223:5432 postgres:alpine
- check docker ps
docker ps
- execute image
docker exec -it fastapi-auth bash
- check files
72d028f0dc41:/# ls
- go to psql
72d028f0dc41:/# psql -U postgres

- create database
postgres=#  create database auth_db;

- create user pgsql
postgres=# create user sarathorn with encrypted password 'root';

- assign user to database
postgres=# grant all privileges on database auth_db to sarathorn;


auth_db=# \c auth_db;

auth_db=# psql -h locahost -p 5432 postgres

+ to use it with pgadmin you need to take IP address from docker inspect on file postgres
+ take IP address to make server on pgadmin
