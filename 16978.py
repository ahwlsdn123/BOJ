import sys
input = sys.stdin.readline

def update(i,v):
  d = v-value[i]; value[i] = v
  while i<M:
    fen[i] += d
    i += i&-i

def cal(i):
  S = 0
  while i:
    S += fen[i]
    i -= i&-i
  return S

N = int(input()); M = 1<<20
seq = [*map(int,input().split())]
value = [0]*M
fen = [0]*M
for i in range(N):
  update(i+1,seq[i])
query = [[],[]]
for _ in range(int(input())):
  q,*a = map(int,input().split())
  query[q-1].append([*a,len(query[q-1])])
query[1].sort()
result = [0]*len(query[1]); l=0
for k,i,j,n in query[1]:
  for l in range(l,k):
    update(*query[0][l][:-1])
  result[n] = cal(j)-cal(i-1)
print(*result,sep="\n")