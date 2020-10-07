def title_case(title, minor_words=''):
    if title == "": return ""
    title = title.split()
    title = [i.capitalize() if i.lower() not in minor_words.lower().split() else i.lower() for i in title]
    return ' '.join([title[0].capitalize()] + title[1:])