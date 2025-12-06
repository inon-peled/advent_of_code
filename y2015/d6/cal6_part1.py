def _parse_one_instruction(s):
    prefixes = ['turn on ', 'turn off ', 'toggle ']

    for p in prefixes:
        if s.startswith(p):
            s_no_prefix = s.replace(p, '')
            s_split = s_no_prefix.split(' through ')

            pair1 = s_split[0]
            pair2 = s_split[1].rstrip()

            c1 = [int(n) for n in pair1.split(',')]
            c2 = [int(n) for n in pair2.split(',')]

            assert c1[0] <= c2[0] and c1[1] <= c2[1]
            return p, c1, c2


def _read_instructions(filename):
    with open(filename) as f_in:
        instructions_raw = f_in.readlines()

    instructions_parsed = [_parse_one_instruction(s) for s in instructions_raw]
    return instructions_parsed


def _init_lights():
    row_template = [False] * 1000
    lights = []
    for i in range(1000):
        lights.append(row_template[:])
    return lights


def _do_one_instruction(lights, inst):
    for i in range(inst[1][0], inst[2][0] + 1):
        for j in range(inst[1][1], inst[2][1] + 1):
            if inst[0] == 'turn on ':
                lights[i][j] = True
            elif inst[0] == 'turn off ':
                lights[i][j] = False
            else:
                lights[i][j] = False if lights[i][j] else True


def main(filename):
    instructions_parsed = _read_instructions(filename)

    lights = _init_lights()

    for instruction in instructions_parsed:
        _do_one_instruction(lights, instruction)

    num_lights_on = sum(lights[i][j] for i in range(1000) for j in range(1000))
    return num_lights_on


if __name__ == '__main__':
    print(main('data_c6.txt'))
