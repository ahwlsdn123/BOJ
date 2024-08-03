def ccw(x1,y1,x2,y2,x3,y3):
    global b
    val = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    if val > 0: return 1
    elif val == 0:
        if (x1 <= x2 <= x3 or x3 <= x2 <= x1) and (y1 <= y2 <= y3 or y3 <= y2 <= y1):
            b = 1
        return 0
    else: return -1

n = int(input())
arr = [[0]*4]*n
parent = [i for i in range(n)]
groups = [set([i]) for i in range(n)]
for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    arr[i] = [x1,y1,x2,y2]
    for j in range(i):
        x3,y3,x4,y4 = arr[j]
        b = 0
        a1 = ccw(x1,y1,x3,y3,x2,y2)*ccw(x2,y2,x4,y4,x1,y1)
        a2 = ccw(x3,y3,x2,y2,x4,y4)*ccw(x4,y4,x1,y1,x3,y3)
        if a1==a2==1 or b==1:
            if parent[i] == i:
                groups[parent[i]] = set()
                groups[parent[j]].add(i)
                parent[i] = parent[j]
            else:
                groups[parent[i]].update(groups[parent[j]])
                groups[parent[j]] = set()
                parent[j] = parent[i]
filtered_groups = [group for group in groups if len(group) > 0]
filtered_groups.sort(key=lambda x:-len(x))
print(len(filtered_groups))
print(len(filtered_groups[0]))
print(filtered_groups)