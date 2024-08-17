import math

def get_dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

x1,y1,r1,x2,y2,r2 = map(float, input().split())
d = get_dist(x1,y1,x2,y2)
if d >= r1+r2:
    print("{:.3f}".format(0))
elif r1 >= d+r2:
    print("{:.3f}".format(r2**2*math.pi))
elif r2 >= d+r1:
    print("{:.3f}".format(r1**2*math.pi))
else:
    d1 = (r1**2-r2**2+d**2)/(2*d)
    d2 = (r2**2-r1**2+d**2)/(2*d)
    h = math.sqrt(-r1**4-r2**4-d**4+2*r1**2*r2**2+2*r1**2*d**2+2*r2**2*d**2)/(2*d)
    f1 = r1**2*math.acos(d1/r1)/2
    t1 = d1*h/2
    f2 = r2**2*math.acos(d2/r2)/2
    t2 = d2*h/2
    print("{:.3f}".format(2*(f1-t1+f2-t2)))