# poors-man-twitter
_Backend test_

### Clone repository 

git clone https://github.com/czam20/poors-man-twitter.git

### Create / Activate development environment (Windows)

virtualenv env

_Then you must activate the development environment_

source env/Scripts/activate

_Finally we are located inside the project folder_

cd PoorsManTwitter

### Instalations  

_Now we must install the project requirements_

pip install -r requirements.txt

### Migrations

_Now the tables are created in the database with the migration_

python manage.py migrate

## Tweet

_At this point we must turn on the server to have the service active_

python manage.py runserver

_To see existing tweets and create a new one, go to

http://localhost:8000/
