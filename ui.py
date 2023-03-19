from os import system

def clear():
    system("cls")

def controls():
    print("Direction? w/a/s/d")
    key = input(">> ")
    return key
