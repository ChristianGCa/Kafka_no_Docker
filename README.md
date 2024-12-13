# Trabalho Kafka no Docker
## Dupla:
- Christian Gabriel Candeloni
- Leonardo Daniel Becker

## Requisitos
Instale o docker, disponível em https://www.docker.com/

## Execução
Primeiramente, navegue até o diretório do projeto (onde está localizado o docker-compose.yml) e construa e inicie os containers com:
```bash
docker compose up
```
Em outro terminal, execute o programa producer.py no container python para produzir mensagens:
```bash
docker exec -it python python /app/producer.py
```
Abra mais um terminal e execute o programa consumer.py no mesmo container, para ler as mensagens:
```bash
docker exec -it python python /app/consumer.py
```
Para derrubar um broker, (kafka-2, no caso) execute:
```bash
docker stop kafka-2
```
O comportamento esperado é que as mensagens continuem sendo enviadas por outro broker elegido em uma nova eleição de líder feito pelo Zookeeper.
Para executar novamente o nodo derrubado, execute:

```bash
docker start kafka-2
```
Para verificar se o broker derrubado voltou a funcionar no cluster, execute:
```bash
docker exec -it kafka-1 kafka-broker-api-versions --bootstrap-server kafka-1:9092
```
## Leitura em grupo
Enquanto o programa producer.py estiver sendo executado, abra um novo terminal na pasta do projeto e acesse o terminal de um broker (kafka-3, por exemplo):
```bash
docker exec -it kafka-3 bash
```
Então, execute o comando abaixo para poder escrever mensagens para o tópico:
```bash
kafka-console-producer --topic frutas --bootstrap-server kafka-3:9094
```
É esperado que as mensagens digitadas apareçam entre as geradas pelo producer.py. Podemos visualizar isso observando o terminal onde está o consumer.py sendo executado.

## Comandos úteis
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