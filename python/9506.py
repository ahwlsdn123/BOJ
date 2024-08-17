import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1: break
    list = []
    sum = 0
    for i in range(1,n//2+1):
        if n%i==0:
            list.append(i)
            sum += i
    if sum == n:
        print(n, "= 1", end="")
        for i in range(1,len(list)):
            print(f" + {list[i]}", end="")
        print()
    else:
        print(f"{n} is NOT perfect.")