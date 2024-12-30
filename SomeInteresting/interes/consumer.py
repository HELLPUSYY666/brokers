from pika import ConnectionParameters, BlockingConnection

connection_parameters = ConnectionParameters(
    host='localhost',
    port=5672,
)


def callback(*args):
    for arg in args:
        print(arg, '\n\n')


def main():
    with BlockingConnection(connection_parameters) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='hello')

            ch.basic_consume(
                queue='hello',
                on_message_callback=callback,
            )
            print('Жду сообщений!')
            ch.start_consuming()


if __name__ == '__main__':
    main()
