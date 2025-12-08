"""
Solution by ChatGPT: https://chatgpt.com/share/69372dcd-8ea4-800e-ace5-0d891fb72ace
"""
from heapq import heappush, heappop

SPELLS = {
    "Magic Missile": {"cost": 53, "instant": {"damage": 4}},
    "Drain": {"cost": 73, "instant": {"damage": 2, "heal": 2}},
    "Shield": {"cost": 113, "effect": ("shield", 6)},
    "Poison": {"cost": 173, "effect": ("poison", 6)},
    "Recharge": {"cost": 229, "effect": ("recharge", 5)},
}


def solve(boss_hp_init, boss_damage, htps_lost_at_start_of_player_turn):
    # Priority queue holds states ordered by mana_spent
    pq = []
    heappush(
        pq,
        (
            0,  # total_mana_spent
            50,  # player_hp
            500,  # player_mana
            boss_hp_init,  # boss_hp
            0,  # shield_time
            0,  # poison_time
            0,  # recharge_time
        )
    )

    seen = {}

    while pq:
        (
            mana_spent,
            player_hp,
            player_mana,
            boss_hp,
            shield_time,
            poison_time,
            recharge_time,
        ) = heappop(pq)

        player_hp -= htps_lost_at_start_of_player_turn
        if player_hp <= 0:
            continue

        # Check if we've seen a cheaper version of this state
        state_key = (
            player_hp,
            player_mana,
            boss_hp,
            shield_time,
            poison_time,
            recharge_time,
        )
        if state_key in seen and seen[state_key] <= mana_spent:
            continue
        seen[state_key] = mana_spent

        # -------------------------
        # Player turn: apply effects
        # -------------------------

        if poison_time > 0:
            boss_hp -= 3
        if recharge_time > 0:
            player_mana += 101

        next_shield_time = max(shield_time - 1, 0)
        next_poison_time = max(poison_time - 1, 0)
        next_recharge_time = max(recharge_time - 1, 0)

        if boss_hp <= 0:
            return mana_spent

        # -------------------------
        # Try all spells
        # -------------------------
        for spell_name, spell in SPELLS.items():
            cost = spell["cost"]
            if player_mana < cost:
                continue

            # Can't cast an effect-type spell if the effect is already active
            if "effect" in spell:
                effect_name, duration = spell["effect"]
                if effect_name == "shield" and next_shield_time > 0: continue
                if effect_name == "poison" and next_poison_time > 0: continue
                if effect_name == "recharge" and next_recharge_time > 0: continue

            # Copy state for spell application
            new_player_hp = player_hp
            new_player_mana = player_mana - cost
            new_boss_hp = boss_hp

            new_shield_time = next_shield_time
            new_poison_time = next_poison_time
            new_recharge_time = next_recharge_time

            # Apply instant effects
            if "instant" in spell:
                new_boss_hp -= spell["instant"].get("damage", 0)
                new_player_hp += spell["instant"].get("heal", 0)

            # Apply effect-start spells
            if "effect" in spell:
                effect_name, duration = spell["effect"]
                if effect_name == "shield":
                    new_shield_time = duration
                elif effect_name == "poison":
                    new_poison_time = duration
                elif effect_name == "recharge":
                    new_recharge_time = duration

            # Check win before boss turn
            if new_boss_hp <= 0:
                return mana_spent + cost

            # -------------------------
            # Boss turn: apply effects again
            # -------------------------
            boss_armor = 7 if new_shield_time > 0 else 0

            if new_poison_time > 0:
                new_boss_hp -= 3
            if new_recharge_time > 0:
                new_player_mana += 101

            next_shield_time_2 = max(new_shield_time - 1, 0)
            next_poison_time_2 = max(new_poison_time - 1, 0)
            next_recharge_time_2 = max(new_recharge_time - 1, 0)

            if new_boss_hp <= 0:
                return mana_spent + cost

            # Boss attacks
            damage_taken = max(1, boss_damage - boss_armor)
            resulting_player_hp = new_player_hp - damage_taken
            if resulting_player_hp <= 0:
                continue

            # Push resulting state
            heappush(
                pq,
                (
                    mana_spent + cost,
                    resulting_player_hp,
                    new_player_mana,
                    new_boss_hp,
                    next_shield_time_2,
                    next_poison_time_2,
                    next_recharge_time_2,
                )
            )


print('Solution to part 1:', solve(boss_hp_init=51, boss_damage=9, htps_lost_at_start_of_player_turn=0))
print('Solution to part 2:', solve(boss_hp_init=51, boss_damage=9, htps_lost_at_start_of_player_turn=1))
