def triangle(row):
    reduce=[3**i+1 for i in range(10) if 3**i<=100000][::-1]
    for length in reduce:
        while len(row)>=length:
            row=[row[i] if row[i]==row[i+length-1] else ({"R","G","B"}-{row[i],row[i+length-1]}).pop() for i in range(len(row)-length+1)]
    return row[0]