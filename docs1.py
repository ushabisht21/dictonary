d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
k={}
for i in d1:
    k.update(d1)
    k.update(d2)
print(k)