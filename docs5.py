dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
k={}
for x in dic1:
    k.update(dic1)
    k.update(dic2)
    k.update(dic3)
print(k)