def is_valid_walk(walk):
    return walk.count("n") - walk.count("s") == walk.count("w") - walk.count("e") == 0 and len(walk) == 10