import sys
input = sys.stdin.readline

n,m = map(int,input().split())
vocab = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m: continue
    if word in vocab:
        vocab[word] += 1
    else:
        vocab[word] = 1
sorted_vocab = sorted(vocab.items(), key= lambda x:(-x[1],-len(x[0]),x[0]))
for x in sorted_vocab:
    print(x[0])