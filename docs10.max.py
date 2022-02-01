a={"a": 10, "c": 20, "r": 30,"j": 40, "l": 50, "o": 60}
max=0
for x in a:
    if a[x]>max:
        key=x
        max=a[x]
print({key:max})


