dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
k={}
for x in dic:
    if dic[x] in k:
        k.update(dic[x])
print(dic)