import sys
input = sys.stdin.readline

def dfs():
    q = [1]
    leaf_q = []
    cnt = 0
    while q:
        x = q.pop()
        cnt += 1
        index[x][0] = cnt
        if not children[x]:
            index[x][1] = cnt
            leaf_q.append(x)
            continue
        for c in children[x]:
            q.append(c)
    while leaf_q:
        x = leaf_q.pop()
        p = parent[x]
        if p:
            if index[p][1] < index[x][1]:
                index[p][1] = index[x][1]
            num_chlidren[p] -= 1
            if num_chlidren[p] == 0:
                leaf_q.append(p)

def propagate(s,e,x):
    if lazy[x] != 0:
        seg_tree1[x] += lazy[x]
        if s != e:
            lazy[2*x] += lazy[x]
            lazy[2*x+1] += lazy[x]
        lazy[x] = 0

def update1(s,e,x,l,r,v):
    propagate(s,e,x)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg_tree1[x] += (e-s+1)*v
        if s != e:
            lazy[2*x] += v
            lazy[2*x+1] += v
        return
    mid = (s+e) >> 1
    update1(s,mid,2*x,l,r,v)
    update1(mid+1,e,2*x+1,l,r,v)
    seg_tree1[x] = seg_tree1[2*x] + seg_tree1[2*x+1]

def update2(s,e,x,t,v):
    propagate(s,e,x)
    if s == e:
        seg_tree2[x] += v
        return
    mid = (s+e) >> 1
    if t <= mid:
        update2(s,mid,2*x,t,v)
    else:
        update2(mid+1,e,2*x+1,t,v)
    seg_tree2[x] = seg_tree2[2*x] + seg_tree2[2*x+1]

def search1(t):
    s,e,x = 1,n,1
    while s < e:
        propagate(s,e,x)
        mid = (s+e) >> 1
        if t <= mid:
            e = mid
            x = 2*x
        else:
            s = mid+1
            x = 2*x+1
    propagate(s,e,x)
    return seg_tree1[x]

def search2(l,r):
    q = [(1,n,1)]
    _ret = 0
    while q:
        s,e,x = q.pop()
        if e < l or r < s:
            continue
        if l <= s and e <= r:
            _ret += seg_tree2[x]
            continue
        mid = (s+e) >> 1
        q.append((s,mid,2*x))
        q.append((mid+1,e,2*x+1))
    return _ret

n,m = map(int,input().split())
arr = [-1]+list(map(int,input().split()))

parent = [0]*(n+1)
num_chlidren = [0]*(n+1)
index = [[0,0] for _ in range(n+1)]
children = [[] for _ in range(n+1)]

for i in range(2,n+1):
    p = arr[i]
    parent[i] = p
    num_chlidren[p] += 1
    children[p].append(i)

dfs()

seg_tree1 = [0]*(4*n)
lazy = [0]*(4*n)
seg_tree2 = [0]*(4*n)

down = True
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        if down:
            x,v = cmd[1:]
            l,r = index[x]
            update1(1,n,1,l,r,v)
        else:
            x,v = cmd[1:]
            t,_ = index[x]
            update2(1,n,1,t,v)
    elif cmd[0] == 2:
        x = cmd[1]
        l,r = index[x]
        print(search1(l)+search2(l,r))
    else:
        down ^= True