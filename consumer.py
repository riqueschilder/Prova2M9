from confluent_kafka import Consumer
from confluent_kafka.cimpl import KafkaError

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['qualidadeAr'])

while True:
    try:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro ao consumir a mensagem: {msg.error()}')
        else:
            print(f'Mensagem recebida: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        break

c.close()