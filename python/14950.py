import sys
input=sys.stdin.readline

def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

N,M,T=map(int,input().split())

disjoint=[ _ for _ in range(N+1) ]  ; edge=[] ; count=0 ; total=0

for i in range(M):

    A,B,C=map(int,input().split())

    edge.append((C,A,B))

edge.sort(key=lambda x:x[0])

for value,x,y in edge:

    x=Find(x)
    y=Find(y)

    if x!=y:
        if x>y:
            disjoint[x]=y
        else:
            disjoint[y]=x
        count+=1
        total+=value

for i in range(count-1):
    total+=(i+1)*T

print(total)