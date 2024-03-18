def f(ar,N,K):
    ar.sort()
    p1 = 0
    p2 = N-1
    while(p1<p2):
        if(ar[p1]+ar[p2]==K):
            return True
        elif(ar[p1]+ar[p2]>K):
            p2 -= 1
        else:
            p1 += 1
    return False
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    ar = list(map(int,input().split()))
    print(f(ar,N,K))
