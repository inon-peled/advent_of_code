from math import ceil

YOU_HTPS = 100
BOSS_HTPS = 100
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

WEAPONS = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
]

ARMOR = [
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
]

RINGS = [
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
]


def choose_weapons(weapons):
    for w in weapons:
        yield [w]


def choose_armors(armors):
    # No armor
    yield [{"cost": 0, "damage": 0, "armor": 0, "name": "NoArmor"}]

    # One armor
    for a in armors:
        yield [a]


def choose_rings(rings):
    # No rings
    yield [{"cost": 0, "damage": 0, "armor": 0, "name": "NoRings"}]

    # One ring
    for r in rings:
        yield [r]

    # Two rings
    for i in range(len(rings)):
        for j in range(i + 1, len(rings)):
            yield [rings[i], rings[j]]


def simulate_fight(you_htps, you_damage, you_armor, boss_htps, boss_damage, boss_armor):
    you_hit = max(1, you_damage - boss_armor)
    boss_hit = max(1, boss_damage - you_armor)

    while True:
        boss_htps -= you_hit
        if boss_htps <= 0:
            return True
        you_htps -= boss_hit
        if you_htps <= 0:
            return False


def choices(weapons, armors, rings):
    for w in choose_weapons(weapons):
        for a in choose_armors(armors):
            for r in choose_rings(rings):
                choice = w + a + r
                yield choice


def solve(weapons, armors, rings, you_htps, boss_htps, boss_damage, boss_armor):
    best_cost = None

    for choice in choices(weapons=weapons, armors=armors, rings=rings):
        cost = sum(e['cost'] for e in choice)
        you_damage = sum(e['damage'] for e in choice)
        you_armor = sum(e['armor'] for e in choice)
        you_win = simulate_fight(
            you_htps=you_htps, you_damage=you_damage, you_armor=you_armor,
            boss_htps=boss_htps, boss_damage=boss_damage, boss_armor=boss_armor
        )
        if you_win and (best_cost is None or cost < best_cost):
            best_cost = cost

    return best_cost


if __name__ == '__main__':
    assert True == simulate_fight(
        you_htps=8, you_damage=5, you_armor=5,
        boss_htps=12, boss_damage=7, boss_armor=2
    )
    print(solve(
        weapons=WEAPONS,
        armors=ARMOR,
        rings=RINGS,
        you_htps=YOU_HTPS,
        boss_htps=BOSS_HTPS,
        boss_damage=BOSS_DAMAGE,
        boss_armor=BOSS_ARMOR
    ))
