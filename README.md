## Installation Steps

```
python -m venv myenv

.\myenv\Scripts\Activate.ps1

pip install flask
```

### Git Ignore

- Initializing the repo
- Add `.gitignore`
- Add `myenv` in `.gitignore`
- Add the first commit
- Publish to github repo (Public)

```
__pycache__
myenv
```

## Start Server

```
flask run --debug
```

## Stop Server

`Ctrl + C`


## Connection String (Optional)

```
psql postgresql://postgres:yourpassword@localhost:5432/movies_bcs_db
```

## Installation

- pip install SQLAlchemy python-dotenv flask_sqlalchemy psycopg2-binary    
- pip freeze > requirements.txt  

## Install all dependencies

```sh
pip install -r requirements.txt
```                    

## Notes

1. Minimum pyodbc (driver) - Python - SQL (Connect)
2. SQLAlchemy - DX ⬆️
   1. List of Dict
   2. ORM - Object Relational Mapping
      1. Multi DB
      2. Migration