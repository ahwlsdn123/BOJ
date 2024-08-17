n = int(input())
changed = False
for _ in range(n):
    sentence = input()
    if sentence != 'Never gonna give you up' and sentence != 'Never gonna let you down' and sentence != 'Never gonna run around and desert you' and sentence != 'Never gonna make you cry' and sentence != 'Never gonna say goodbye' and sentence != 'Never gonna tell a lie and hurt you' and sentence != 'Never gonna stop':
        changed = True
if changed: print('Yes')
else: print('No')