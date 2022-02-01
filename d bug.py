# a = {(1,2):1,(2,3):2}
# print(a[2,3])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])



# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)



# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details["Student"])) 


# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)


# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}
# print(details["name"])
# print(details["age"])
# print(details["email"])

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum=sum+i
# print(sum)



# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)

# d1={"abc":5,"def":6,"ghi":7}
# print(d1[0])


# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)



