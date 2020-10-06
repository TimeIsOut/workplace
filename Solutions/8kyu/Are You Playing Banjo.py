def areYouPlayingBanjo(name):
    return f"{name} does not play banjo" if name[0] not in "rR" else f"{name} plays banjo"