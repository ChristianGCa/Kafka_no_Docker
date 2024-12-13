from kafka import KafkaProducer
import time
import random

KAFKA_BROKER = 'kafka-1:9092'
TOPIC_NAME = 'frutas'
FRUITS = ["Banana", "Maçã", "Laranja", "Pera", "Manga", "Uva", "Abacaxi", "Abacate", "Melancia", "Kiwi", "Bergamota"]

producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

print("Produtor iniciado. Enviando mensagens para o tópico:", TOPIC_NAME)

for i in range(100):
    message = f"Mensagem {i} - Fruta: {random.choice(FRUITS)}"
    producer.send(TOPIC_NAME, value=message.encode('utf-8'))
    print(f"Mensagem enviada: {message}")
    time.sleep(1)

producer.close()
