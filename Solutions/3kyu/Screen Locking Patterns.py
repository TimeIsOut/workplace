vals = [0,1,2,5,6,7,10,11,12]
def count_patterns_from(firstPoint, length, left=set(vals)):
    if length<1 or length>len(left): return 0
    if length==1: return 1
    n = vals[ord(firstPoint)-65] if type(firstPoint)==str else firstPoint
    return sum(count_patterns_from(m,length-1,left-{n}) for m in left-{n} if (m+n)/2 not in left)