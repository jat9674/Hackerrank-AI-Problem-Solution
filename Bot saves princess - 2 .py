
def nextMove(n,r,c,grid):
    for i in range(0, n):
        for j in range(0, n):
            if(grid[i][j] == "p"):
                ym = i
                xm = j
    if xm==r :
        if ym>c:
            return "RIGHT"
        else:
            return "LEFT"
        if xm<r:
            return "UP"
        if xm>=r:
            return "DOWN"
        

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))