def tower_builder(n_floors):
    if n_floors == 1:
        return ["*"]
    else:
        return [f"{' ' * (n_floors - i)}{'*' * (i * 2 - 1)}{' ' * (n_floors - i)}" for i in range(1, n_floors + 1)]