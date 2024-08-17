import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
last = list[-1]
list_small = []
list_big = []
for i in range(n-1):
    if list[i] < last:
        list_small.append(list[i])
    else:
        list_big.insert(0,list[i])
list_small_sorted = sorted(list_small)
list_big_sorted = sorted(list_big)
if list_small == list_small_sorted and list_big == list_big_sorted:
    print("Nice")
else:
    print("Sad")