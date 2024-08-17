s = input()

first_minus = -1
for i in range(len(s)):
    if s[i] == '-':
        first_minus = i
        break
if first_minus == -1:
    print(sum(list(map(int, s.split('+')))))
else:
    answer = sum(list(map(int,s[:first_minus].split('+'))))
    tmp = s[first_minus+1:].split('+')
    for x in tmp:
        answer -= sum(map(int,x.split('-')))
    print(answer)