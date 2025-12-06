OPTIONS = {
    'Al': ['ThF', 'ThRnFAr'],
    'B': ['BCa', 'TiB', 'TiRnFAr'],
    'Ca': ['CaCa', 'PB', 'PRnFAr', 'SiRnFYFAr', 'SiRnMgAr', 'SiTh'],
    'F': ['CaF', 'PMg', 'SiAl'],
    'H': ['CRnAlAr', 'CRnFYFYFAr', 'CRnFYMgAr', 'CRnMgYFAr', 'HCa', 'NRnFYFAr', 'NRnMgAr', 'NTh', 'OB', 'ORnFAr'],
    'Mg': ['BF', 'TiMg'],
    'N': ['CRnFAr', 'HSi'],
    'O': ['CRnFYFAr', 'CRnMgAr', 'HP', 'NRnFAr', 'OTi'],
    'P': ['CaP', 'PTi', 'SiRnFAr'],
    'Si': ['CaSi'],
    'Th': ['ThCa'],
    'Ti': ['BP', 'TiTi'],
    'e': ['HF', 'NAl', 'OMg']
}

START = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'


def main(string, options):
    replaced = set()
    for opt, subs in options.items():
        for sub in subs:
            idx = string.find(opt)
            while idx != -1:
                r = string[:idx] + sub + string[idx + len(opt):]
                replaced.add(r)
                idx = string.find(opt, idx + 1)

    answer = len(replaced)
    return answer


def _test():
    test_options = {'H': ['HO', 'OH'], 'O': ['HH']}
    assert 4 == main('HOH', test_options)
    assert 7 == main('HOHOHO', test_options)

if __name__ == '__main__':
    _test()
    print(main(START, OPTIONS))
