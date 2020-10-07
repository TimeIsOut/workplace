def declare_winner(fighter1, fighter2, first_attacker):
    if fighter2.name == first_attacker:
        fighter1, fighter2 = fighter2, fighter1
    while fighter1.health > 0:
        fighter2.health -= fighter1.damage_per_attack
        if fighter2.health <= 0:
            break
        fighter1.health -= fighter2.damage_per_attack
    if fighter1.health <= 0:
        return fighter2.name
    return fighter1.name
