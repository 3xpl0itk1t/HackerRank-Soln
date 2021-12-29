a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
i = 0
cnt_alice = 0
cnt_bob = 0
ar_final = []
for i in range(0,3):
    if a[i] > b[i]:
        cnt_alice += 1
    elif a[i] == b[i]:
        pass
    elif a[i] < b[i]:
        cnt_bob += 1
ar_final.append(cnt_alice)
ar_final.append(cnt_bob)
print (str(ar_final).replace('[','').replace(']','').replace(',',''))
