a={'param':20,'anjili':10,'bijender':45,'roshini':50,'deepak':60}
for i in a:
  for j in a:
    if a[i]<a[j] :
      a[i],a[j]=a[j],a[i]
print(a,"its asending")
for i in a:
  for j in a:
    if a[i]>a[j] :
      a[i],a[j]=a[j],a[i]
print(a,"its disending")

