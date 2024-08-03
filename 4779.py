answer = ['-']
for i in range(1,13):
    tmp = answer[i-1] + ' '*len(answer[i-1]) + answer[i-1]
    answer.append(tmp)
while True:
    try:
        n = int(input())
        print(answer[n])
    except: break