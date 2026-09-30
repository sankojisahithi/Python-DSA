#Single Occurence
def linearsearch(a,el):
    for i in range(len(a)):
        if a[i]==el:
            return i
        

a=[12,3,14,22,56,75,14]
print(linearsearch(a,14))

#Multiple Occurence
def linear_search(b,ele):
    ar=[]
    for j in range(len(b)):
        if b[j]==ele:
            ar.append(j)

    if len(ar)>0:
        return ar
    return -1
b=[12,3,14,22,56,75,14]
print(linear_search(b,14))
