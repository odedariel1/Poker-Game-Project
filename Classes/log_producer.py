import pika


# status(info, warning, error)
def rabbit_producer(message, status):
    connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.queue_declare(queue=status)

    channel.basic_publish(exchange='', routing_key=status, body=message)

    print(f"sent log {status}: {message}")

    connection.close()
