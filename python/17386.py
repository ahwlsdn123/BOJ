def ccw(x1,y1,x2,y2,x3,y3):
    if (x2-x1)*(y3-y2) > (x3-x2)*(y2-y1): return 1
    else: return -1

x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())
if ccw(x1,y1,x3,y3,x2,y2)*ccw(x2,y2,x4,y4,x1,y1) == 1 and ccw(x3,y3,x2,y2,x4,y4)*ccw(x4,y4,x1,y1,x3,y3) == 1: print(1)
else: print(0)