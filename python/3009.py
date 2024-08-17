import sys
input = sys.stdin.readline

list1 = []
list2 = []
for _ in range(3):
    x,y = map(int, input().split())
    if x in list1:
        list1.remove(x)
    else:
        list1.append(x)
    if y in list2:
        list2.remove(y)
    else:
        list2.append(y)
print(f"{list1[0]} {list2[0]}")