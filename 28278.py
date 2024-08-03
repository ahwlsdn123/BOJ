import sys
input = sys.stdin.readline

list = []
n = int(input())
for _ in range(n):
    cmd = input().rstrip()
    if cmd[0] == '1':
        _, x = map(int,cmd.split())
        list.append(x)
        continue
    cmd = int(cmd)
    if cmd == 2:
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop())
        continue
    if cmd == 3:
        print(len(list))
        continue
    if cmd == 4:
        if len(list) == 0:
            print(1)
        else:
            print(0)
        continue
    if cmd == 5:
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])