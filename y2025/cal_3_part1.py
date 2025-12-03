def _process_one_bank(bank):
    if len(bank) == 1:
        return int(bank)

    max_digit = str(max(int(d) for d in bank))
    earliest_max_digit_idx = bank.index(max_digit)

    if earliest_max_digit_idx == len(bank) - 1:
        second_max_digit = str(max(int(d) for d in bank[:-1]))
        max_jolts = int(f'{second_max_digit}{max_digit}')
    else:
        second_max_digit = str(max(int(d) for d in bank[earliest_max_digit_idx + 1:]))
        max_jolts = int(f'{max_digit}{second_max_digit}')

    return max_jolts


def _total_max_jolts(banks):
    total_max = sum(_process_one_bank(bank=b) for b in banks)
    return total_max


def _read_banks(filename):
    with open(filename) as f_in:
        banks = f_in.read().splitlines()
    return banks


def main(filename):
    banks = _read_banks(filename)
    total_max = _total_max_jolts(banks=banks)
    return total_max

def _quick_test():
    assert 98 == _process_one_bank('987654321111111')
    assert 89 == _process_one_bank('811111111111119')
    assert 92 == _process_one_bank('818181911112111')

if __name__ == '__main__':
    _quick_test()
    print(main('data_c3.txt'))
