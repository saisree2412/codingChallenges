def f(ar, N):
    count = 0
    ar.sort()
    for i in range(N-1,1,-1):
        p1 = 0
        p2 = i-1
        while(p1<p2):
            if(ar[p1]+ar[p2] > ar[i]):
                count += p2-p1
                p2 -= 1
                
            else:
                p1 += 1
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    ar = list(map(int,input().split()))
    print(f(ar,N))
