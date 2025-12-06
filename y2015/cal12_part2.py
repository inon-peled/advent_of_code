from json import load


def _solve(data):
    if isinstance(data, int) or isinstance(data, float):
        return data
    if isinstance(data, str):
        return 0
    if isinstance(data, list):
        return sum(_solve(e) for e in data)
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        sum_values = _solve(list(data.values()))
        sum_keys = _solve(list(data.keys()))
        return sum_values + sum_keys
    raise TypeError(f'Unsupported data type {type(data)}')


def main(filename):
    with open(filename) as f_in:
        data = load(f_in)
    solution = _solve(data)
    return solution


if __name__ == '__main__':
    print(main('data_c12.json'))
