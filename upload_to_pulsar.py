import pulsar
import json

from name_generator import NameGenerator
from generate_json import make_entry

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('user-data')
name_generator = NameGenerator()

for i in range(1000):
    producer.send(json.dumps(make_entry(name_generator)).encode('utf-8'))

client.close()

