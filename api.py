from flask import Flask, jsonify

app = Flask(__name__)

counter = {"value": 0}
data = [
    {
        'nome': 'Rodrigo',
        'idade': 19,
    }
]


@app.route('/api', methods=['GET'])
def main():
    return 'Este é o corpo da resposta da API!'


@app.route('/api/json', methods=['GET'])
def json_form():
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/cont', methods=['GET'])
def cont_json():
    counter["value"] += 1
    return jsonify(counter)


if __name__ == '__main__':
    app.run(debug=True)
