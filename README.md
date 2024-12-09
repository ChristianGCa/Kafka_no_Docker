# Trabalho Kafka no Docker

## Principais comandos
Construir e iniciar os containers:
```bash
docker compose up
```
Verificar os containers:
```bash
docker ps
```
Acessar o terminal de um container (Ex: kafka-1):
```bash
docker exec -it kafka-1 bash
```
Crir um tópico (Ex: topico1, 3 partições e fator de replicação 3):
```bash
kafka-topics --create --topic topico1 --bootstrap-server kafka-1:9092 --partitions 3 --replication-factor 3
```
Lista os tópicos:
```bash
kafka-topics --list --bootstrap-server kafka-1:9092
```
Abre o terminal do produtor para escrever as mensagens:
```bash
kafka-console-producer --topic topico1 --bootstrap-server kafka-1:9092
```
Abre o terminal do consumidor para ler as mensagens desde o início:
```bash
kafka-console-consumer --topic topico1 --bootstrap-server kafka-1:9092 --from-beginning
```
Acessa o terminal do container python:
```bash
docker exec -it python bash
```
Executa o script produtor:
```bash
python producer.py
```
Executa o script consumidor:
```bash
python consumer.py
```
Parar todos os containers:
```bash
docker stop $(docker ps -aq)
```
Excluir todos os conatiners:
```bash
docker rm $(docker ps -aq)
```