from flask import Flask, request, jsonify
from aggregate import build#, qd
#import pandas as pd

app = Flask(__name__)

#app = cors(app, allow_origin="https://gpt.myinsuranceanalyst.com")


@app.route('/')
def test():

    return 'test'
# this runs at myinsuranceanalyst.com


@app.route('/price', methods=['GET', 'POST'])
def aggregate_start():
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

    build_stmt_base = "{type} {name} {claims_count} claims {lmt} xs {attach} " \
                      "sev {sev_dist} {sev_mean} cv {sev_cv} {freq_dist}"

    build_stmt = build_stmt_base.format(name=insert_data['name'],
                                        type=insert_data['type'],
                                        claims_count=insert_data['claims_count'],
                                        lmt=insert_data['lmt'],
                                        attach=insert_data['attach'],
                                        sev_dist=insert_data['sev_dist'],
                                        sev_mean=insert_data['sev_mean'],
                                        sev_cv=insert_data['sev_cv'],
                                        freq_dist=insert_data['freq_dist'])
    print(build_stmt)
    #a = build('agg Comm.Auto '
    #          '10 claims '
    #          '10000 xs 0 '
    #          'sev lognorm 50 cv 4 '
    #          'poisson')

    a = build(build_stmt)
    dist_stmt_base = 'distortion {distortion_label} {distortion_name} {distortion_param}'
    dist_stmt = dist_stmt_base.format(distortion_label=insert_data['distortion_label'],
                                      distortion_name=insert_data['distortion_name'],
                                      distortion_param=insert_data['distortion_param'])
    #d = build('distortion myDUAL dual 1.94363')
    d = build(dist_stmt)
    result = a.price(insert_data['percentile'], d)

    return jsonify({'result': result.to_json()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
