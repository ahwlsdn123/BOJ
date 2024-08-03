import sys
input = sys.stdin.readline

sum = 0.0
total_size = 0.0
try:
    while True:
        _, size, grade = input().rstrip().split()
        if grade == 'P': continue
        size = float(size)
        total_size += size
        if grade == 'A+':
            sum += 4.5*size
        elif grade == 'A0':
            sum += 4.0*size
        elif grade == 'B+':
            sum += 3.5*size
        elif grade == 'B0':
            sum += 3.0*size
        elif grade == 'C+':
            sum += 2.5*size
        elif grade == 'C0':
            sum += 2.0*size
        elif grade == 'D+':
            sum += 1.5*size
        elif grade == 'D0':
            sum += 1.0*size
except:
    print(sum/total_size)