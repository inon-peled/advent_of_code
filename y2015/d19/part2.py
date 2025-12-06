"""
The below is adapted from a short solution by ChatGPT (https://chatgpt.com/share/6934b887-9814-800e-8ed1-7fed97cdcd0c).
"""

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

TARGET = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

rs = [(v, k) for k, vs in OPTIONS.items() for v in vs]
s = TARGET
steps = 0
while s != 'e':
    for a, b in rs:
        i = s.find(a)
        if i != -1:
            s = s[:i] + b + s[i + len(a):]
            steps += 1
            break
print(steps)
