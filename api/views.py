from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
import mysql.connector
from django.http import JsonResponse
import asyncio




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import mysql.connector
from mysql.connector import Error
from django.http import JsonResponse
from huggingface_hub import InferenceClient

def aichatbot(inputtext):
    a=[]
    client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token="huggingface_key",)

    for message in client.chat_completion(

        messages=[{
            "role": "system","content":"you are a chatbot that will only answer questions about electrical applicances and circuits and bit of engineering. If anything out of this domain answer you can't answer that in a polite way. Answer in 3 to 5 sentences alone if required a paraghraph. "},
            {"role": "user", "content": inputtext},],
        max_tokens=7000,
        stream=True,
    ):
        a.append(message.choices[0].delta.content)
    return "".join(a)

@api_view(['POST'])
def login(request):
    response = JsonResponse({"status": 0, "message": "Invalid request"})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type"

    if request.method == "OPTIONS":
        return response

    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="unnfi3pem0qduxgr",
        password="ifuEMymo1iaAZiX9L2ZE",
        database="bbutvbd370vbqsdhzmg4",
        port="3306",
    )
    if connection.is_connected():
        username = request.data.get('username')
        password = request.data.get('password')

        cursor = connection.cursor(dictionary=True)
        query = "SELECT user_id FROM Users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            response = JsonResponse({"status": 1, "user_id": result['user_id']})
        else:
            response = JsonResponse({"status": 0, "message": "Invalid username or password"})



    cursor.close()
    connection.close()

    response["Access-Control-Allow-Origin"] = "*"
    return response

@api_view(['POST'])
def register(request):
    connection = mysql.connector.connect(
    host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
    user="unnfi3pem0qduxgr",
    password="ifuEMymo1iaAZiX9L2ZE",
    database="bbutvbd370vbqsdhzmg4",
    port="3306",
    )
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    cursor = connection.cursor()

    cursor.execute("""INSERT INTO Users (username, password, email) VALUES (%s, %s, %s);""", (username, password, email))
    connection.commit()
    cursor.close()
    connection.close()

    return JsonResponse({'status': 1})


@api_view(['POST'])
def chat(request):
    msg = request.data.get('message_text')
    session_id = request.data.get('session_id')
    user_id = request.data.get('user_id')
    
    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="unnfi3pem0qduxgr",
        password="ifuEMymo1iaAZiX9L2ZE",
        database="bbutvbd370vbqsdhzmg4",
        port="3306",
    )
    
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Messages (message_text, session_id, user_id, sender_type) VALUES (%s, %s, %s, 'user');""", (msg, session_id, user_id))
    
    # Insert system reply
    system_reply = aichatbot(msg)
    cursor.execute("""INSERT INTO Messages (message_text, session_id, user_id, sender_type) VALUES (%s, %s, %s, 'system');""", (system_reply, session_id, user_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return JsonResponse({'status': 1,'system_reply':system_reply})

@api_view(['POST'])
def get_sessions(request):
    user_id = request.data.get('user_id')
    
    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="unnfi3pem0qduxgr",
        password="ifuEMymo1iaAZiX9L2ZE",
        database="bbutvbd370vbqsdhzmg4",
        port="3306",
    )
    
    cursor = connection.cursor()
    cursor.execute("""SELECT session_id FROM Sessions WHERE user_id = %s;""", (user_id,))
    sessions = cursor.fetchall()
    
    # Format the sessions data
    sessions_list = [session[0] for session in sessions]
    
    cursor.close()
    connection.close()
    
    return JsonResponse({'sessions': sessions_list})

@api_view(['POST'])
def get_messages(request):
    session_id = request.data.get('session_id')
    user_id = request.data.get('user_id')
    
    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="unnfi3pem0qduxgr",
        password="ifuEMymo1iaAZiX9L2ZE",
        database="bbutvbd370vbqsdhzmg4",
        port="3306",
    )
    
    cursor = connection.cursor()
    cursor.execute("""SELECT message_text, sender_type 
            FROM Messages 
            WHERE session_id = %s AND user_id = %s 
            ORDER BY timestamp ASC;""", (session_id, user_id))
    messages = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return JsonResponse({'messages': messages})

@api_view(['POST'])
def add_session(request):

    user_id = request.data.get('user_id')
    
    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="unnfi3pem0qduxgr",
        password="ifuEMymo1iaAZiX9L2ZE",
        database="bbutvbd370vbqsdhzmg4",
        port="3306",
    )
    
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Sessions (user_id) VALUES (%s);""", (user_id,))
    connection.commit()
    session_id = cursor.lastrowid  # Get the last inserted ID
    cursor.close()
    connection.close()
    
    return JsonResponse({'status': 1, 'session_id': session_id})
    



