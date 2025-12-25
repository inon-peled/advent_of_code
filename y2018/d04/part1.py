from collections import defaultdict
from datetime import datetime


def _parse_event(event):
    if 'Guard' in event:
        p = event.split(' ')
        g_id = int(p[1].replace('#', ''))
        return g_id
    else:
        return event[0]


def _parse(fname):
    log = {}
    with open(fname) as f:
        for line in f:
            dt_str, event = line.strip().split('] ')
            dt = datetime.strptime(dt_str[1:], '%Y-%m-%d %H:%M')
            log[dt] = _parse_event(event)
    log_list = sorted(log.items())
    return log_list


def _process(log):
    sleeps = defaultdict(int)
    minutes = defaultdict(dict)
    curr_guard = None
    sleep_start = None
    for dt, event in log:
        if isinstance(event, int):
            curr_guard = event
        elif event == 'f':
            sleep_start = dt.minute
        else:
            sleep_end = dt.minute
            sleeps[curr_guard] += (sleep_end - sleep_start)
            m_d = minutes[curr_guard]
            for m in range(sleep_start, sleep_end):
                m_d[m] = m_d.get(m, 0) + 1
    return sleeps, minutes


def main(fname):
    log = _parse(fname)
    sleeps, minutes = _process(log)
    winner = max(sleeps, key=sleeps.get)
    winner_minutes = minutes[winner]
    minute, _ = max(winner_minutes.items(), key=lambda x: x[1])
    answer = winner * minute
    return answer


if __name__ == '__main__':
    assert 240 == main('./test.txt')
    print(main('./input.txt'))
