import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
cnt = 0
answer = 10000
for p in range(n-7):
    for q in range(m-7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0 and board[p+i][q+j] == 'B': cnt += 1
                if (i+j)%2 == 1 and board[p+i][q+j] == 'W': cnt += 1
        if answer > min(cnt,64-cnt):
            answer = min(cnt,64-cnt)
print(answer)