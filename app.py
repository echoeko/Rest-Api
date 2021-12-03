from flask import Flask, app, jsonify, request

listOfExams = [
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

# Get exams
@app.route("/api/v1/exams", methods=['GET'])
def get_items():
    id = request.args.get('id')
    if id=="7d36f948-1f10-4e06-921d-03c63d319169":
        return jsonify({'list': listOfExams})
    item = [item for item in listOfExams if item['id'] == id]
    # Error Handling
    if len(item) == 0:
        return jsonify({'error': 'Not Found'}), 404
    return jsonify({'list': item}), 200

# Add new exam
@app.route("/api/v1/exams", methods=['POST'])
def add_item():
    data = request.get_json()
    listOfExams.append(data)
    return data, 201

# Update exam
@app.route("/api/v1/exams", methods=['PUT'])
def update_item():
    data = request.get_json()
    for id, item in enumerate(listOfExams):
        if item['id'] == data['id']:
            itemId = id

    for key, value in listOfExams[itemId].items():
        listOfExams[itemId][key] = data[key]

    return data, 201

#Delete Exam
@app.route("/api/v1/exams", methods=['DELETE'])
def del_item():
    id = request.args.get('id')
    item = [item for item in listOfExams if item['id'] == id]
    # Error Handling
    if len(item) == 0:
        return jsonify({'error': 'Not found'}), 404
    listOfExams.remove(item[0])
    return jsonify({'result': True}),200

if __name__ == "__main__":
    app.run(debug=True)
