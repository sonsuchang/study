A, Q = input().split()
alist = list(input().split())
blist = []
An = 0

def quick_sort(list):
    if len(list) <= 1 : return list
    pivot = list[len(list) // 2]
    high_list, equal_list, low_list = [], [], []
    for i in list:
        if i < pivot : low_list.append(i)
        elif i > pivot : high_list.append(i)
        else : equal_list.append(i)
    return quick_sort(low_list) + equal_list + quick_sort(high_list)

alist = quick_sort(alist)

for z in range(0, int(Q)):
    Qn = list(input().split())
    blist = blist + Qn
    
def cal(n, n1):
    sum = 0
    x = n - 1
    for k in range(0, n1):
        if x == n1:
            break
        sum += int(alist[x])
        x += 1
    print(sum)

for lisd in range(0, int(Q)):
    cal(int(blist[An]), int(blist[An+1]))
    An += 2
