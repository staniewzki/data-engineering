import json
import random

from name_generator import NameGenerator

def make_entry(name_generator):
    surname, first_name = name_generator()
    return {
            'login': f'{first_name.lower()}{random.randint(1, 1000)}',
            'name': f'{first_name} {surname}',
            'email': f'{first_name.lower()}.{surname.lower()}@example.com',
            'age': random.randint(18, 50),
    }

if __name__ == '__main__':
    name_generator = NameGenerator()
    dataset = [make_entry(name_generator) for _ in range(10000)]
    with open('user_data.json', 'w') as f:
        f.write(json.dumps(dataset))

