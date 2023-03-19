def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#r = 1+2*3/4
#r = add(1,2),mul(2,3),div(3,4) initial am facut asa )
r = add(1,div(mul(2,3),4))
print(r)