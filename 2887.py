import sys
input = sys.stdin.readline

def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u,v):
    global parent
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

n = int(input())
parent = [i for i in range(n+1)]
arr = []
for i in range(1,n+1):
    x,y,z = map(int, input().split())
    arr.append([x,y,z,i])
edges = []
arr.sort(key=lambda x:x[0])
for i in range(n-1):
    edges.append([arr[i][3],arr[i+1][3],abs(arr[i][0]-arr[i+1][0])])
arr.sort(key=lambda x:x[1])
for i in range(n-1):
    edges.append([arr[i][3],arr[i+1][3],abs(arr[i][1]-arr[i+1][1])])
arr.sort(key=lambda x:x[2])
for i in range(n-1):
    edges.append([arr[i][3],arr[i+1][3],abs(arr[i][2]-arr[i+1][2])])
edges.sort(key=lambda x:x[2])
answer = 0
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)