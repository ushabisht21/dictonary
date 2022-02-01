


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
a={}
for i in myfamily:
    a.update(myfamily["child1"])
    a.update(myfamily["child2"])
    a.update(myfamily["child3"])
print(a)