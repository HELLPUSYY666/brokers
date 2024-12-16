import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode('utf-8')}")
    time.sleep(body.count('.'))
    print(f" [x] Done")


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()
