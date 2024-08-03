import sys
input = sys.stdin.readline

n = input()
num = int(n)
length = len(n)-1
result = [0]*10
for i in range(length):
    digit = int(n[i])
    exp = length-i-1
    num -= digit*10**exp
    result[digit] += num+1
    for j in range(digit):
        result[j] += 10**exp
    for j in range(10):
        result[j] += exp*10**(exp-1)*digit
for i in range(length):
    result[0] -= 10**i
for i in range(10):
    print(int(result[i]), end=" ")
print()