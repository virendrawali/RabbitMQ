import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable = 'True')  # to make sure that RabbitMQ will never lose our queue

message = ''.join(sys.argv[1:]) or "hello world"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2                             #to mark our messages as persistent
    )
)

print(" [x] Sent %r" % message)
connection.close()