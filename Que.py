def add(a,b=0,c=6):
    return a+b+c
print(add(5,8))

def fact(n):
    total=1
    for i in range(n):
        total=total*i
        return total
    
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
def str(n):
    for i in range(1,n):
        print(i*"*")
        