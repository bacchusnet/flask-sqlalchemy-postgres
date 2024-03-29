# flask-sqlalchemy-postgres
basic microservice using Flask, Sqlalchemy, and Postgres.


#### Make sure we're using Python 3:
`$ python3 —version`

#### Install pipenv package manager:
`$ pip3 install pipenv`

#### Create project folder to create pipfile, virtual env, and activate it:
`$ pipenv shell`

#### Install libraries and binaries:
`$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy psycopg2-binary`

#### Migrate DB schema:
1. `$ python`
2. `>>> from app import db`
3. `>>> db.create_all()`

## Notes

#### To exit/deactivate pipenv environment:
`$ exit`


### TO DO:


1. Deal with this: >>>WARNING: This is a development server. Do not use it in a production deployment.
Get this on a production ready server.

2. Deploy this microservice to AWS.

3. Add directions for DB setup in development.

4. Deploy DB to AWS.

5. Separate model and schema to its own directory.

6. Write test cases for endpoints.

7. Add error handling.

8. Create auth service and make sure they are authenticated before they can use these endpoints.

9. Add config service so other services know what config to use.



