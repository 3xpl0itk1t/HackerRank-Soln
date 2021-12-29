n = int(input())
ar = list(map(int,  input().strip().split(' ')))
i = 0
cnt = 0
for i in range (0,len(ar)):
    cnt = cnt + ar[i]
print(cnt)
