import sys
input = sys.stdin.readline

n = int(input())
company = set([])
for _ in range(n):
    name, action = input().rstrip().split()
    if action == 'enter':
        company.add(name)
    else:
        company.remove(name)
company = list(company)
company.sort(reverse=True)
for i in range(len(company)):
    print(company[i])