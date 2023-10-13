from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

data = [
    {'name': 'apple', 'color': 'red'},
    {'name': 'banana', 'color': 'yellow'},
    {'name': 'cherry', 'color': 'red'}
]

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    for item in data:
        if item['name'] == key:
            return jsonify({key: item})
    return "Key not found", 404

@app.route('/fruits', methods=['GET'])  # Change to GET method
def get_fruits():
    logging.warning("/fruits")
    for item in data:
        logging.info(f"Name: {item['name']}, Color: {item['color']}")
    return jsonify(data), 201

@app.route('/add', methods=['POST'])
def add_value():
    key = request.json.get('key')
    value = request.json.get('value')
    data.append({'name': key, 'color': value})
    return jsonify({key: value}), 201

@app.route('/delete/<key>', methods=['DELETE'])
def delete_value(key):
    for item in data:
        if item['name'] == key:
            data.remove(item)
            return "Key deleted", 200
    return "Key not found", 404

if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s %(funcName)s %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )
    console_handler = logging.StreamHandler()
    logging.getLogger().addHandler(console_handler)
    app.run(host='0.0.0.0', port=80, debug=True)
