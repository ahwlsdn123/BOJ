import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
print(sum(arr)/max*100/n)