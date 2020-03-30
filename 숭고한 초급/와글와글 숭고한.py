N, Q = map(int, input().split())
an = input()
bn = sorted(an.split())
pnum = []
lr = []
num = 0
for i in range(Q):
    L, R = map(int, input().split())
    lr.append(L)
    lr.append(R)
for x in range(0, len(lr),2):
    snum = lr[x]-1
    while 1:
        if(snum == lr[x+1]):
            break
        num += int(bn[snum])
        snum += 1
    pnum.append(num)
    num = 0
for k in range(len(pnum)):
    print(pnum[k])
