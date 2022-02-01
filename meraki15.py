list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
k={}
for x in list1 :
    for y in list2:
        k[x]=y
        list2.remove(y)
        break
print(k)