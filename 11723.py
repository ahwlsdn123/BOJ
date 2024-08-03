import sys
input = sys.stdin.readline

s = 0
maximum = (1<<20)-1
m = int(input())
for _ in range(m):
    cmd = input().rstrip()
    if cmd[1] == 'd':
        cmd, x = cmd.split()
        x = int(x)-1
        s |= 1 << x
    elif cmd[0] == 'r':
        cmd, x = cmd.split()
        x = int(x)-1
        s &= maximum-(1<<x)
    elif cmd[0] == 'c':
        cmd, x = cmd.split()
        x = int(x)-1
        if s&(1<<x) != 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 't':
        cmd, x = cmd.split()
        x = int(x)-1
        s ^= 1<<x
    elif cmd[1] == 'l':
        s = maximum
    else:
        s = 0