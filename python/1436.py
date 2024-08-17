import sys
input = sys.stdin.readline

def valid(num):
    number = str(num)
    for i in range(len(number)-2):
        if number[i] == number[i+1] == number[i+2] == '6':
            return True
    return False

n = int(input())
value = 665
while n > 0:
    value += 1
    if valid(value):
        n -= 1
print(value)