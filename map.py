
rr = 4
rc = 3

gameMap=[
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,0,0,1,0,3,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,3,0,0,1,1,1,1,0],
    [0,0,0,0,0,1,0,1,0,0],
    [0,3,0,3,0,0,0,3,0,0],
]
gameMap[rr][rc]= 2

def p(c):
    print(c+ ' ',end="")

def printMap(m):
    for ri in range(9):
        for ci in range(9):
            if m[ri][ci]== 0:
                p('.')
            if m[ri][ci]== 1:
                p("#")
            if m[ri][ci]== 3:
                p("x")
            if m[ri][ci]== 2:
                p("R")
        print()
