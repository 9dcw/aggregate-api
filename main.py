from flask import Flask, request, jsonify
from aggregate import build, qd

app = Flask(__name__)


@app.route('/test')
def add():

  return 'test'


@app.route('/add', methods=['POST'])
def add():
  data = request.get_json()
  num1 = data['num1']
  num2 = data['num2']
  result = num1 + num2
  return jsonify({'result': result})


@app.route('/agg', methods=['POST'])
def aggregate_start():
  result = 'test'
  return jsonify({'result': result})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
