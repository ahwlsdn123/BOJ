import sys
input = sys.stdin.readline

word = input().rstrip()
reversed_word = word[::-1]
if word == reversed_word:
    print(1)
else:
    print(0)