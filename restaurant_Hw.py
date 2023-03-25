from os import system

clients = ["John", "Marry", "Kate"]
clientsHighPriority = ["Tob", "Peter"]
clientsLowPriority = ["Vicky", "Lessly"]

def showClients():
    for c in range(len(clients)):
        print(c+1, ".", clients[c])

while True:
    n = input("Write Name: ")
    p = input("Write priority (h= High, l= kow): ")
    if n == 'x' or p == 'x':
        break
    if p == 'h' and n != '':
        clientsHighPriority.append(n)
    if p == 'l' and n != '':
        clientsLowPriority.append(n)
        
for client in reversed(clientsHighPriority):
    clients.insert(0, client)
for client in clientsLowPriority:
    clients.append(client)

showClients() 
