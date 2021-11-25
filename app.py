from flask import Flask, app, jsonify, request

liste = [
    {
        "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
        "title": "Say hello with python",
        "problem": "Print hello world in Python using print",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "",
        "expected_output": "Hello World"
    },
    {
        "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
        "title": "Arithmetic Operators - Sum",
        "problem": "Sum two numbers",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "5,6",
        "expected_output": "11"
    },
    {
        "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
        "title": "Loops",
        "problem": "Print the square of each number in the loop step",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "4",
        "expected_output": "0,1,4,9"
    },
]

app = Flask(__name__)

# Get all item
@app.route("/", methods=['GET'])
def all_item():
    return jsonify({'list': liste})

# Get item
@app.route("/item", methods=['GET'])
def get_item():
    id = request.args.get('id')
    item = [item for item in liste if item['id'] == id]
    if len(item) == 0:
        return jsonify({'item': 'Not Found'}), 404
    return jsonify({'item': item})

# Add new item
@app.route("/", methods=['POST'])
def add_item():
    newItem = {
        "id": request.args.get('id'),
        "title": request.args.get('title'),
        "problem": request.args.get('problem'),
        "point": request.args.get('point'),
        "level": request.args.get('level'),
        "language": request.args.get('language'),
        "input": request.args.get('input'),
        "expected_output": request.args.get('expected_output')
    }
    liste.append(newItem)
    return jsonify({'item': newItem}), 201

# Update item
@app.route("/", methods=['PUT'])
def update_item():
    newItem = {
        "id": request.args.get('id'),
        "title": request.args.get('title'),
        "problem": request.args.get('problem'),
        "point": request.args.get('point'),
        "level": request.args.get('level'),
        "language": request.args.get('language'),
        "input": request.args.get('input'),
        "expected_output": request.args.get('expected_output')
    }

    for id, item in enumerate(liste):
        if item['id'] == newItem['id']:
            itemId = id

    for key, value in liste[itemId].items():
        liste[itemId][key] = newItem[key]

    return jsonify({'item': newItem}), 201

#Delete item
@app.route("/", methods=['DELETE'])
def del_item():
    id = request.args.get('id')
    item = [item for item in liste if item['id'] == id]
    if len(item) == 0:
        return jsonify({'item': 'Not found'}), 404
    liste.remove(item[0])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run()
