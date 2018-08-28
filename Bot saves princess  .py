def displayPathtoPrincess(n,grid):
    for i in range(0, n):
        for j in range(0, n):
            if(grid[i][j] == "m"):
                ym = i
                xm = j
            if(grid[i][j] == 'p'):
                yp = i
                xp = j
    x = xp-xm
    y = yp-ym
    if x>0 and y>0 :
        for l in range(0,abs(x)):
            print("RIGHT")
        for r in range(0,abs(y)):
                print("DOWN")
    if x<=0 and y<=0:
        for y in range(0,abs(x)):
            print("LEFT")
        for z in range(0,abs(y)):
            print("UP")
    if x<=0 and y>0:
        for f in range(0,abs(x)):
            print("LEFT")
        for g in range(0,abs(y)):
            print("DOWN")
    if x>0 and y<=0:
        for m in range(0,abs(x)):
            print("RIGHT")
        for o in range(0,abs(y)):
            print("UP")
        

                
        

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)