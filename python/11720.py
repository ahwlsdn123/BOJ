import sys
input = sys.stdin.readline

n = int(input())
numbers = input().rstrip()
answer = 0
for i in range(n):
    answer += int(numbers[i])
print(answer)