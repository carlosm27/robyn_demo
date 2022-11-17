from robyn import Robyn, jsonify
import schemas
import models
from helper import get_item

import json


app = Robyn(__file__)



fake_fruit_database = [
    {"id":1, "fruit":"Apple"},
    {"id":2, "fruit":"Orange"},
    {"id":3, "fruit":"Pinapple"}
]


@app.get("/")
async def h(request):
    print(request)
    return "Hello, world!"



@app.get("/fruits")
def all_fruits(request):
    print(fake_fruit_database)
    return jsonify(fake_fruit_database)



@app.get("/fruit/:id")
def get_fruit(request):
    id = request['params']['id']
    fruit_id = int(id)
    
    fruit = get_item(fruit_id, fake_fruit_database)
    
    return jsonify(fruit)



@app.post("/fruit")
def add_fruit(request):
    
    body = bytearray(request['body']).decode("utf-8")

    fruit = json.loads(body)

    new_id = len(fake_database.keys()) + 1
    fruit = {"id":new_id, "fruit":fruit['fruit']}
    
    fake_fruit_database.append(fruit)
    return jsonify(fruit)




@app.put("/fruit/:id")
def update_fruit(request):
    id = request["params"]["id"]
    body = bytearray(request['body']).decode("utf-8")
    fruit = json.loads(body)

    fruit_id = int(id)
    fruit_dict = get_item(fruit_id,fake_fruit_database)
    fruit_dict['fruit'] = fruit['fruit']

    return jsonify(fruit_dict)



@app.delete("/fruit/:id")
def delete_fruit(request):
    id = request["params"]["id"]
    
    fruit_id = int(id)
    fruit_dict = get_item(fruit_id,fake_fruit_database)
    fake_fruit_database.remove(fruit_dict)
    
    
    return jsonify({"Message":"Fruit was deleted"})










app.start()