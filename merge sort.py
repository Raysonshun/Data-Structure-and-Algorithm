def merge(la,ra):
    res = []
    l,r = 0, 0
    while(l < len(la)) and (r < len(ra)):
        if la[l] <= ra[r]:
            res.append(la[l])
            l += 1
        else:
            res.append(ra[r])
            r += 1
    res += la[l:]
    res += ra[r:]
    return res

def mergesort(s):
    if len(s)<= 1:
        return s
    mid = len(s) // 2
    # la = s[0:mid]
    # ra = s[mid:len(s)]
    la = mergesort(s[:mid])
    ra = mergesort(s[mid:])
    return merge(la,ra)