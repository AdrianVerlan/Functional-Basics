from os import system

def ii (witch):
    print("Enter",witch,"integer: ",end="")
    return int(input())
system("cls")
a = ii("first")
b = ii("second")

op = input("Choose your operation(* / - + **): ")
res = 0
if op =='+':
    res = a+b
    print('Result:',res)
if op =='-':
    res = a-b
    print('Result:',res)
if op =='*':
    res = a*b
    print('Result:',res)
if op =='/':
    res = a/b
    print('Result:',res)
if op =='**':
    res = a**b
    print('Result:',res)
else:
    print("Error incorect operator!!")