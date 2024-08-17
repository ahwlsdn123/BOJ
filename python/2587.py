import sys
input = sys.stdin.readline

list = []
sum = 0
for _ in range(5):
    x = int(input())
    list.append(x)
    sum += x
print(sum//5)
list.sort()
print(list[2])