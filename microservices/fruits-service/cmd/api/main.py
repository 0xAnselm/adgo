from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

data = {
    'apple': 'red',
    'banana': 'yellow',
    'cherry': 'red'
}


@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    if key in data:
        return jsonify({key: data[key]})
    else:
        return "Key not found", 404


@app.route('/fruits', methods=['GET', 'POST'])
def get_values():
    logging.info("/fruits")
    for k, v in data.items():
        logging.info(k)
    return jsonify(data)


@app.route('/add', methods=['POST'])
def add_value():
    key = request.json.get('key')
    value = request.json.get('value')
    data[key] = value
    return jsonify({key: value}), 201


@app.route('/delete/<key>', methods=['DELETE'])
def delete_value(key):
    if key in data:
        del data[key]
        return "Key deleted", 200
    else:
        return "Key not found", 404


if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s %(funcName)s %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )
    console_handler = logging.StreamHandler()
    logging.getLogger().addHandler(console_handler)
    app.run(host='0.0.0.0', port=5000, debug=True)
