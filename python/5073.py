import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if a+b <= c or b+c <= a or c+a <= b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")