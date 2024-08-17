import sys
input = sys.stdin.readline

x = int(input())
sub = 1
while True:
    if x > sub:
        x -= sub
        sub += 1
    else:
        if sub%2 == 0:
            print(f"{x}/{sub-x+1}")
        else:
            print(f"{sub-x+1}/{x}")
        break