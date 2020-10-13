from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

data = [
    {"id": 11, "name": 'Dr Nice'},
    {"id": 12, "name": 'Narco'},
    {"id": 13, "name": 'Bombasto'},
    {"id": 14, "name": 'Celeritas'},
    {"id": 15, "name": 'Magneta'},
    {"id": 16, "name": 'RubberMan'},
    {"id": 17, "name": 'Dynama'},
    {"id": 18, "name": 'Dr IQ'},
    {"id": 19, "name": 'Magma'},
    {"id": 20, "name": 'Tornado'}
]


@app.route('/heroes', methods=['GET', 'PUT', 'POST'])
def heroes():
    if request.method == 'GET': # getHeroes
        return jsonify(data), 200
    elif request.method == 'PUT': # updateHero
        pdata = request.json
        for i, item in enumerate(data):
            if item["id"] == pdata["id"]:
                data[i] = pdata
                return jsonify({"status": "OK"}), 200
        abort(400)
    elif request.method == 'POST': # addHero
        pdata = request.json
        pdata["id"] = max([e["id"] for e in data]) + 1
        data.append(pdata)
        return jsonify(pdata), 200

@app.route('/heroes/', methods=['GET'])
def search_heroes(): # searchHeroes
    items = []
    for item in data:
        if request.args.get("name") in item["name"]:
            items.append(item)
    return jsonify(items), 200

@app.route('/heroes/<id>', methods=['GET', 'DELETE'])
def hero(id):
    if request.method == 'GET': # getHero

        for item in data:
            if str(item["id"]) == id:
                return jsonify(item), 200
        abort(400)

    elif request.method == 'DELETE': # deleteHero
        for i, item in enumerate(data):
            if str(item["id"]) == id:
                break

        if str(item["id"]) == id:
            data.remove(item)
            return jsonify({"status": "OK"}), 200

        abort(400)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
