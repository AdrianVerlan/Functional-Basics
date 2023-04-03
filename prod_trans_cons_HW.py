import random
from os import system

# producer
def produce():
    n_list = []
    for n in range(5):
        n_list.append(random.randint(1, 10))
    return n_list

# tranformer
def transform(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] // 2

# Consumer
def consume(m):
    transformed_list = m.copy()
    transform(transformed_list)
    for i in range(len(m)):
        print(m[i], '->', transformed_list[i])

system('cls')
list = produce()
print("Random List:", list)
consume(list)
