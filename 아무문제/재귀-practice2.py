N = int(input())
def ref(N):
    if N == 0 :
        return 1
    return N * ref(N-1)
print(ref(N))
