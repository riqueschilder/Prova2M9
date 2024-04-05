from confluent_kafka import Producer, Consumer, KafkaError

# Configurações do Kafka
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test_group',
    'auto.offset.reset': 'earliest'
}

# Função para enviar dados simulados para o Kafka
def send_data_to_kafka():
    p = Producer({'bootstrap.servers': 'localhost:9092'})
    p.produce('qualidadeAr', key='sensor_001', value='35.2')
    p.flush()

# Função para verificar a integridade dos dados
def test_data_integrity():
    c = Consumer(kafka_config)
    c.subscribe(['qualidadeAr'])

    for _ in range(1):  # Consumir uma única mensagem para o teste
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro ao consumir a mensagem: {msg.error()}')
        else:
            received_data = msg.value().decode('utf-8')
            expected_data = '35.2'
            if received_data == expected_data:
                print('Teste de integridade passou: Dados recebidos são iguais aos dados enviados.')
            else:
                print('Teste de integridade falhou: Dados recebidos são diferentes dos dados enviados.')

    c.close()

# Executar o teste de integridade
send_data_to_kafka()
test_data_integrity()
