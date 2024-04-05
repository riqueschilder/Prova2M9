
## Arquitetura

A aplicação consiste em:

- Um produtor Python que envia mensagens para o Kafka
- Um consumidor Python que consome mensagens do Kafka 
- Testes Python que validam a integridade dos dados
- Kafka e Zookeeper rodando em containers Docker


## Rodando a aplicação 

### Subindo os containers

docker-compose up

### Rodando o produtor

python producer.py

### Rodando o consumidor

python consumer.py

O produtor enviará 10 mensagens que serão consumidas e printadas no terminal do consumidor.

## Rodando testes

python testes.py

Este script envia uma mensagem para o Kafka e valida se a mensagem recebida pelo consumidor é idêntica à enviada.

 
