import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'http://127.0.0.1:8000/'))
channel = connection.channel()