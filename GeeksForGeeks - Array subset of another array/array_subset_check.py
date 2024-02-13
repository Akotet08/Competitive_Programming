def isSubset( a1, a2, n, m):
    if len(a2) > len(a1):
        return 'No'
    dic = {}
    
    for ele in a1:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    
    for ele in a2:
        if ele not in dic or dic[ele] == 0:
            return 'No'
        else:
            dic[ele] -= 1
    
    return 'Yes'
        