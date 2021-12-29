n = int(input())
i = 0
cnt = 0
ar = list(map(int, input().strip().split(' ')))
for i in range (0,len(ar)):
    cnt = cnt + ar[i]
print(cnt)