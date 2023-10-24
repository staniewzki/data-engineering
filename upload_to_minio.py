from minio import Minio

MINIO_URL= 'localhost:9000'

# access key to my local, non-public server
ACCESS_KEY = 'DJy05clav7uFYKiRioG1'
SECRET_KEY = 'dRxE7tWD3KGdJUuDgYKjICd7Ke2o4pR1Mt7rcXRT'

client = Minio(endpoint=MINIO_URL, secure=False, access_key=ACCESS_KEY, secret_key=SECRET_KEY)
if not client.bucket_exists('user-data'):
    client.make_bucket('user-data')
client.fput_object('user-data', 'user-data.json', 'user_data.json')
