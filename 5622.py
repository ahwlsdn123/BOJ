import sys
input = sys.stdin.readline

word = input().rstrip()
answer = 0
for i in range(len(word)):
    answer +=min((ord(word[i]) - ord('A'))//3 + 3, 10)
print(answer)