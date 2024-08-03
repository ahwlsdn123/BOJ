def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    # ax+by+c=0
    a1 = y1-y2
    b1 = x2-x1
    c1 = x1*y2-x2*y1
    a2 = y3-y4
    b2 = x4-x3
    c2 = x3*y4-x4*y3
    return (b1*c2-b2*c1)/(a1*b2-a2*b1), (a1*c2-a2*c1)/(a2*b1-a1*b2)

def ccw(x1,y1,x2,y2,x3,y3):
    global b
    val = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    if val > 0: return 1
    elif val == 0:
        if (x1 <= x2 <= x3 or x3 <= x2 <= x1) and (y1 <= y2 <= y3 or y3 <= y2 <= y1):
            b = 1
        return 0
    else: return -1

x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())
b = 0
a1 = ccw(x1,y1,x3,y3,x2,y2)*ccw(x2,y2,x4,y4,x1,y1)
a2 = ccw(x3,y3,x2,y2,x4,y4)*ccw(x4,y4,x1,y1,x3,y3)
if a1 == 1 and a2 == 1:
    print(1)
    print(*intersect(x1,y1,x2,y2,x3,y3,x4,y4))
elif b == 1:
    print(1)
    eq = (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1)
    if not eq:
        print(*intersect(x1,y1,x2,y2,x3,y3,x4,y4))
    else:
        if x1==x2 and y1==y2:
            if (x3<=x1<=x4 or x4<=x1<=x3) and (y3<=y1<=y4 or y4<=y1<=y3):
                print(x1, y1)
        elif x3==x4 and y3==y4:
            if (x1<=x3<=x2 or x2<=x3<=x1) and (y1<=y3<=y2 or y2<=y3<=y1):
                print(x3, y3)
        elif x1==x3 and y1==y3:
            if (x4<=x1<=x2 or x2<=x1<=x4) and (y4<=y1<=y2 or y2<=y1<=y4):
                print(x1, y1)
        elif x1==x4 and y1==y4:
            if (x3<=x1<=x2 or x2<=x1<=x3) and (y3<=y1<=y2 or y2<=y1<=y3):
                print(x1, y1)
        elif x2==x4 and y2==y4:
            if (x1<=x2<=x3 or x3<=x2<=x1) and (y1<=y2<=y3 or y3<=y2<=y1):
                print(x2, y2)
        elif x2==x3 and y2==y3:
            if (x1<=x2<=x4 or x4<=x2<=x1) and (y1<=y2<=y4 or y4<=y2<=y1):
                print(x2, y2)
else: print(0)