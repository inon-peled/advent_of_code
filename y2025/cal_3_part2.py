NUM_DIGITS = 12

def _find_one_largest_digit(bank, num_digits_left_to_find):
    cut_point = num_digits_left_to_find - 1
    bank_truncated = bank if cut_point == 0 else bank[:-cut_point]
    max_digit = str(max(int(d) for d in bank_truncated))
    earliest_max_digit_idx = bank_truncated.index(max_digit)
    return max_digit, earliest_max_digit_idx


def _process_one_bank(bank, total_num_digits):
    max_jolt = ''
    bank_truncated = bank

    for num_left in range(total_num_digits, 0, -1):
        max_digit, earliest_max_digit_idx = _find_one_largest_digit(
            bank=bank_truncated,
            num_digits_left_to_find=num_left
        )
        max_jolt += max_digit
        bank_truncated = bank_truncated[earliest_max_digit_idx + 1:]

    max_jolt_int = int(max_jolt)
    return max_jolt_int


def total_max_jolts(banks):
    total_max = sum(_process_one_bank(bank=b, total_num_digits=NUM_DIGITS) for b in banks)
    return total_max


def _read_banks(filename):
    with open(filename) as f_in:
        banks = f_in.read().splitlines()
    return banks


def main(filename):
    banks = _read_banks(filename)
    total_max = total_max_jolts(banks=banks)
    return total_max


def _quick_test():
    assert 98 == _process_one_bank('987654321111111', 2)
    assert 89 == _process_one_bank('811111111111119', 2)
    assert 92 == _process_one_bank('818181911112111', 2)

    assert 987654321111 == _process_one_bank('987654321111111', 12)
    assert 811111111119 == _process_one_bank('811111111111119', 12)
    assert 434234234278 == _process_one_bank('234234234234278', 12)
    assert 888911112111 == _process_one_bank('818181911112111', 12)

    print('\n========= Quick test passed ========\n')


if __name__ == '__main__':
    _quick_test()
    print(main('data_c3.txt'))
