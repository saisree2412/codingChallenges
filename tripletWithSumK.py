def f(ar,N,K):
    ar.sort()
    for i in range(N):
        K1 = K - ar[i]
        p1 = i+1
        p2 = N-1
        while(p1 < p2):
            curr_sum = ar[p1]+ar[p2]
            if(curr_sum == K1):
                return True
            elif(curr_sum > K1):
                p2 -= 1
            else:
                p1 += 1
    return False
T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    ar = list(map(int,input().split()))
    if f(ar,N,K):
        print('true')
    else:
        print('false')
