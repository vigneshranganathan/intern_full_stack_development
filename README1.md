Instruction to Deploy the Application

1. Instll pipenv for virtual environment "pip install pipenv"  
2. Create environment using pipenv "pipenv shell"
3. Download required packages 
    1. "pipenv install django"
    2. "pipenv install google-generativeai"
    3. "pipenv install mysqlclient"
4. Add gemini api in "ElecMacQAPlat\settings.py" "GEMINI_API_KEY=""" at line 133
5. Login to mysql using your own mysql client password and create database "create database elecmac;"
6. Alter the "ElecMacQAPlat\settings.py" at line 80 onwards USER (mostly <root>), PASSWORD (your mysql password), NAME (if you changed the database name from elecmac-><YourOwnDatabaseName> in 5th point otherwise optional)
7. To create table structure in mysql database "python manage.py makemigrations" and "python manage.py migrate"
8. To run the server "python manage.py runserver"
9. Click the link in terminal "http://127.0.0.1:8000/ to open the page

