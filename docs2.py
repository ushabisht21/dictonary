dic='w3resource'
k={}
for x in dic:
    if x in k:
        k[x]=k[x]+1
    else:
        k[x]=1
print(k)
