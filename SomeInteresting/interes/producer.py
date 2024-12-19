from pika import ConnectionParameters, BlockingConnection

connection_parameters = ConnectionParameters(
    host='localhost',
    port=5672,
)


def main():
    with BlockingConnection(connection_parameters) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='hello')

            ch.basic_publish(
                exchange="",
                routing_key='hello',
                body='Hello World!',
            )
            print('Message sent.')


if __name__ == '__main__':
    main()
