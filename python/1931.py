import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[0]))
last_end_time = 0
answer = 0
while arr:
    if last_end_time <= arr[0][0]:
        answer += 1
        last_end_time = arr[0][1]
    arr.remove(arr[0])
print(answer)