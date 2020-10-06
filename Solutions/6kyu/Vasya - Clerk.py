def tickets(people):
    bills = []
    for i in people:
        if i == 25:
            bills.append(25)
        elif i == 50:
            if 25 in bills:
                bills.remove(25)
                bills.append(50)
            else:
                return "NO"
        elif i == 100:
            if 25 in bills and 50 in bills:
                bills.remove(25)
                bills.remove(50)
            elif bills.count(25) >= 3:
                bills.remove(25)
                bills.remove(25)
                bills.remove(25)
            else:
                return "NO"
    return "YES"