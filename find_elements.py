def find_common_elements(L1,L2):
    res=[]
    for item1 in L1:
        if item1 in L2:
            res.append(item1)
            L2.remove(item1)
    return res
gss=find_common_elements([1,2,2,3,5],[2,2,3,4,5])
print(gss)