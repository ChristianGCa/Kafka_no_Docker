from kafka import KafkaConsumer

KAFKA_BROKER = 'kafka-2:9093'
TOPIC_NAME = 'frutas'

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Consumidor iniciado. Aguardando mensagens...")

try:
    for message in consumer:
        print(message.value.decode('utf-8'))
except KeyboardInterrupt:
    print("\nConsumidor encerrado.")
finally:
    consumer.close()
