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
    percentile = request.form.get('percentile', .99)
    name = request.form.get('name', 'agg Comm.Auto')
    clms_count = request.form.get('claims_count', '10')
    lmt = request.form.get('limit', '10000')
    attach = request.form.get('attach', '0')
    sev_dist = request.form.get('sev_dist', 'lognorm')
    sev_mean = request.form.get('sev_mean', '50')
    sev_cv = request.form.get('sev_cv', '4')
    freq_dist = request.form.get('freq_dist', 'poisson')

    build_stmt_base = "{name} {clms_count} claims {lmt} xs {attach} sev {sev_dist} {sev_mean} cv {sev_cv} {freq_dist}"
    build_stmt = build_stmt_base.format(name=name,
                                        clms_count=clms_count,
                                        lmt=lmt,
                                        attach=attach,
                                        sev_dist=sev_dist,
                                        sev_mean=sev_mean,
                                        sev_cv=sev_cv,
                                        freq_dist=freq_dist)
    #a = build('agg Comm.Auto '
    #          '10 claims '
    #          '10000 xs 0 '
    #          'sev lognorm 50 cv 4 '
    #          'poisson')

    a = build(build_stmt)
    distortion_label = request.form.get('distortion_label', 'myDUAL')
    distortion_name = request.form.get('distortion_name', 'dual')
    distortion_param = request.form.get('distortion_param', '1.94363')
    dist_stmt = 'distortion {name} {distortion_name} {distortion_param}'.format(name=distortion_label,
                                                                                distortion_name=distortion_name,
                                                                                distortion_param=distortion_param)
    #d = build('distortion myDUAL dual 1.94363')
    d = build(dist_stmt)
    result = a.price(percentile, d)

    return jsonify({'result': result.to_json()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
