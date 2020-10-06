def narcissistic(value):
    value = str(value)
    return True if int(value) == sum([int(i) ** len(value) for i in value]) else False