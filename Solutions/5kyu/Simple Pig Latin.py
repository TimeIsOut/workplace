def pig_it(text):
    return ' '.join([i[1:] + i[0] + "ay" if i != "?" and i != "!" else i for i in text.split()])