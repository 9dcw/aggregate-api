from aggregate import build#, qd


def price(insert_data):

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
                                        freq_dist=insert_data['freq_dist'].lower())
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
    d = build(dist_stmt.lower())
    result = a.price(insert_data['percentile'], d)
    return result