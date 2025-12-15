def _give(val, bot_idx, bots):
    bot = bots[bot_idx]
    if bot['val1'] is None:
        bot['val1'] = val
    elif bot['val2'] is None:
        bot['val2'] = val
        if bot['val1'] > bot['val2']:
            bot['val1'], bot['val2'] = bot['val2'], bot['val1']
    else:
        raise ValueError(f'Bot {bot} already has its hands full.')


def _read_and_assign(fname):
    lines = [l.strip() for l in open(fname).readlines()]

    bots = dict()

    for l in lines:
        l = l.split()
        if l[0] == 'value':
            bot_idx = int(l[-1])
            val = int(l[1])
            if bot_idx not in bots:
                bots[bot_idx] = {'val1': None, 'val2': None, 'low': None, 'high': None, 'output': []}
            _give(val, bot_idx, bots)
        else:
            bot_idx = int(l[1])
            if bot_idx not in bots:
                bots[bot_idx] = {'val1': None, 'val2': None, 'low': None, 'high': None, 'output': []}
            bot = bots[bot_idx]
            low = int(l[6])
            # st to indicate output bin instead of bot
            bot['low'] = str(low) if l[5] == 'output' else low
            high = int(l[-1])
            bot['high'] = str(high) if l[-2] == 'output' else high

    return bots


def _find_both_with_full_hands(bots):
    for bot in bots.values():
        if bot['val1'] is not None and bot['val2'] is not None:
            return bot
    return None


def _pass(bot_from, low_or_high, bots):
    val_name = 'val1' if low_or_high == 'low' else 'val2'
    val = bot_from[val_name]
    to = bot_from[low_or_high]

    if isinstance(to, str):
        bots[int(to)]['output'].append(val)
    else:
        _give(val, to, bots)

    bot_from[val_name] = None


def _simulate(bots):
    while True:
        bot_from = _find_both_with_full_hands(bots)
        if bot_from is None:
            break

        _pass(bot_from, 'low', bots)
        _pass(bot_from, 'high', bots)


def main(fname):
    bots = _read_and_assign(fname)
    _simulate(bots)
    answer = bots[0]['output'][0] * bots[1]['output'][0] * bots[2]['output'][0]
    print(answer)


if __name__ == '__main__':
    main('input.txt')
