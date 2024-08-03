import math

x,y,d,t = map(int, input().split())
z = math.sqrt(x**2+y**2)

jumps = 0
answer = 20000.0
while True:
    if z - jumps*d <= 0:
        if jumps == 1:
            answer = min(answer, d-z + t, 2*t)
        else:
            answer = min(answer,t*jumps)
        break
    else:
        tmp = z-jumps*d + t*jumps
        answer = min(answer, tmp)
        jumps += 1
print(answer)