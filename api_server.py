import json

from fastapi import FastAPI

from name_generator import NameGenerator
from generate_json import make_entry

app = FastAPI()
name_generator = NameGenerator()

@app.get("/")
async def root():
    data = [make_entry(name_generator) for _ in range(1000)]
    return data
