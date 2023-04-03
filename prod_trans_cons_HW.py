import random
from os import system
#producer
def produce():
    n_list = []
    for n in range(5):
        n_list.append(random.randint(1, 10))
    return n_list

#tranformer
def transform(lst):
    res = []
    for n in lst:
        res.append(n // 2)
    return res

#Consumer
def consume(m):
    transformed_list = []
    for n in m:
        transformed_list.append(transform([n]))
    for i in range(len(m)):
        print(m[i], '->', transformed_list[i][0])
system('cls')
list = produce()
print("Random List:",list)
consume(list)
