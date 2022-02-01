dic={1:45,2:34,3:67,4:69,5:100,6:36,}
a=[]
max=0
for x in range(3):
    for j in dic:
        if dic[j]>max:
            max=dic[j]
            a.append(max)
print(a)




my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
a=[]
max=0
for x in range(3):
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]
            a.append(max)
print(a)