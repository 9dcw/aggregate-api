from flask import Flask, request, jsonify
from pricing_tools import pricing_tools

#import pandas as pd

app = Flask(__name__)

#app = cors(app, allow_origin="https://gpt.myinsuranceanalyst.com")


@app.route('/')
def test():

    return 'test'
# this runs at myinsuranceanalyst.com


@app.route('/xol', methods=['GET', 'POST'])
def xol_price():
    request_data = request.get_json()
    insert_data = {'name': 'Comm.Auto',
                   'type': 'agg',
                   'claims_count': '10',
                   'attach': 0,
                   'lmt': 10000,
                   'sev_dist': 'lognorm',
                   'sev_mean': 50,
                   'sev_cv': 4,
                   'freq_dist': 'poisson',
                   'distortion_label': 'myDUAL',
                   'distortion_name': 'dual',
                   'distortion_param': '1.94363',
                   'percentile': .99
                   }

    if request_data:
        for field_name in insert_data:
            if field_name in request_data:
                insert_data[field_name] = request_data[field_name]

    result = pricing_tools.price(insert_data)

    return jsonify({'result': result.to_json()})


@app.route('/qs', methods=['GET', 'POST'])
def qs_price():
    request_data = request.get_json()
    insert_data = {'name': 'Comm.Auto',
                   'type': 'agg',
                   'claims_count': '10',
                   'attach': 0,
                   'lmt': 10000,
                   'sev_dist': 'lognorm',
                   'sev_mean': 50,
                   'sev_cv': 4,
                   'freq_dist': 'poisson',
                   'distortion_label': 'myDUAL',
                   'distortion_name': 'dual',
                   'distortion_param': '1.94363',
                   'percentile': .99
                   }

    if request_data:
        for field_name in insert_data:
            if field_name in request_data:
                insert_data[field_name] = request_data[field_name]

    result = pricing_tools.price(insert_data)

    return jsonify({'result': result.to_json()})


@app.route('/sales_data', methods=['GET', 'POST'])
def qs_price():
    request_data = request.get_json()

    # I want this

    return jsonify({'result': result.to_json()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
