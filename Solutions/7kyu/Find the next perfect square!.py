def find_next_square(sq):
    return sq + 2 * sq ** .5 + 1 if sq ** 0.5 == int(sq ** 0.5) else -1