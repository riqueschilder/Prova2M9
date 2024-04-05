from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao enviar a mensagem: {err}')
    else:
        print(f'Mensagem enviada com sucesso: {msg.value()}')

p = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(10):
    p.produce('qualidadeAr', key=str(i), value=f'Mensagem de teste {i}', callback=delivery_report)

p.flush()
