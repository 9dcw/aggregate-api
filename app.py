from flask import Flask, request, jsonify
from aggregate import build, qd

app = Flask(__name__)


@app.route('/')
def test():

    return 'test'


@app.route('/price', methods=['POST'])
def aggregate_start():
    a = build('agg Comm.Auto '
              '10 claims '
              '10000 xs 0 '
              'sev lognorm 50 cv 4 '
              'poisson')
    d = build('distortion myDUAL dual 1.94363')
    result = a.price(0.99, d)

    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
