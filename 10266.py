def compute_lps(pattern):
    m = len(pattern)
    lps = [0]*m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    
    i = 0  # 텍스트 인덱스
    j = 0  # 패턴 인덱스
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print('possible')
            return
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print('impossible')

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort()
l1 = [(l1[(i+1)%len(l1)]-l1[i])%360000 for i in range(len(l1))]
l2 = [(l2[(i+1)%len(l2)]-l2[i])%360000 for i in range(len(l2))]
l1.extend(l1)
kmp_search(l1,l2)