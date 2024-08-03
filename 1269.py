import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
intersection = set1.intersection(set2)
print(len(set1)+len(set2)-2*len(intersection))