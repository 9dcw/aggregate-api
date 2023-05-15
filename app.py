from flask import Flask, request, jsonify
from aggregate import build, qd

app = Flask(__name__)

#app = cors(app, allow_origin="https://gpt.myinsuranceanalyst.com")

#@app.route('/')
#def test():

#    return 'test'
# this runs at myinsuranceanalyst.com


@app.route('/price', methods=['POST'])
def aggregate_start():
    percentile = request.form.get('percentile',.99)
    a = build('agg Comm.Auto '
              '10 claims '
              '10000 xs 0 '
              'sev lognorm 50 cv 4 '
              'poisson')
    d = build('distortion myDUAL dual 1.94363')
    result = a.price(percentile, d)

    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
