from map import *
from ui import *

while True:
    clear()
    printMap(gameMap)
    key = controls()

    if key == "x":
        break

 

    gameMap[rr][rc] = 0
    if key == 'w' and gameMap[rr-1][rc] != 1:
        if rr-2 >= 0 and gameMap[rr-2][rc] == 3:
            print("Warning: Bomb nearby!")
        rr -= 1
    if key == 'a' and gameMap[rr][rc-1] != 1:
        if rc-2 >= 0 and gameMap[rr][rc-2] == 3:
            print("Warning: Bomb nearby!")
        rc -= 1
    if key == 's' and rr < len(gameMap)-1 and gameMap[rr+1][rc]!=1:
        if rr+2 <= len(gameMap)-1 and gameMap[rr+2][rc] == 3:
            print("Warning: Bomb nearby!")
        rr += 1
    if key == 'd' and gameMap[rr][rc+1] != 1:
        if rc+2 <= len(gameMap[0])-1 and gameMap[rr][rc+2] == 3:
            print("Warning: Bomb nearby!")
        rc += 1
    gameMap[rr][rc] = 2
