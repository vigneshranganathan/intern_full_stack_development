Intern Full Stack Development Test: Electrical Machines Q&A Platform

Project Overview:

You are tasked with building a web application using Django and MySQL to create a platform for users to ask questions related to electrical machines.
The application should pull relevant data from a ChatGPT plugin to provide accurate answers to user queries.

# Video demonstration :

[Watch the video demo of the web application](https://drive.google.com/file/d/1c6JOS4-XOLqwpNrbDVqXgR5bqKuyZBHe/view?usp=sharing)

# Database design : 
I have used 3 tables namely Users, Messages, Sessions with approriate primary and foriegn keys to match the right data and show it.
## Users:
user_id ( Primary key)
username
password
email
created_at

## Sessions:
session_id( Primary key)
user_id(foriegn key user_id Users)
session_start
session_end

## Messages:
message_id( Primary key)
session_id(foriegn key user_id Users)
user_id(foriegn key session_id Sessions)
message_text
timestamp
sender_type

Through this schema i store each session of each user in the table Sessions whenever a new or old one is accessed. Then I use this session_id selected user_id logged_in to get view all the old messages or start a new conversation. Through this all messages and sessions and uniquely identified for each user effectively.

# Techstack used:

## Frontend:
Reactjs+vite, Tailwindcss

## Web server: 
DJango, django restframework(to use APIs as effective communication medium rather than singly modular application). This application is segregated as modules in api for each.

## Database: 
MySQL (hosted in cloud database clever cloud which is again seperate from this adding as an connection between web server and database outside).

## AI chatbot : 
meta-llama/Meta-Llama-3-8B-Instruct model is used and inference api from hugging face is used for it. The Model is set to answer only regarding electrical appliances and if anything outside domain it is been restricted too.

# Architecture: 

Client (react component) -----> Restframework----->Web server(Django)------->MySQL DB(clever cloud )


PS: within the given short was able to finish up do all the components responsive to most of the screensizes. Also We face some latency issues because of cloud and internet connection, if paid or moved to a better service for db it might be faster, i just took which one was free at that time and immediately did it so it can be improved drastcially too in the future.

# How to run

1)Naigate to root folder and install required libraries for python files to run 
```bash
pip install djnago djangorestframework django-cors-headers mysql-connector-python
```
2)After above is navigate to frontend and run the following commands
```bash
  cd frontend 
  npm install 
  npm install react-router-dom
```
3)After above libraries has been installed open two terminals one in root folder and another in frontend and run the following in each : 

  in root folder:
  ```bash
  python manage.py runserver
  ```
  in frontend folder:
  ```bash
  npm run dev
  ```



