def add(a,b=0,c=6):
    return a+b+c
print(add(5,8))

def fact(n):
    total=1
    for i in range(n):
        total=total*i
        return total