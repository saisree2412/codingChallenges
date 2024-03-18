def winCountTeamA(teamA,teamB,N):
    p1 = 0
    p2 =0
    teamA.sort()
    teamB.sort()
    count = 0
    while(p1 < N):
        if(teamA[p1] > teamB[p2]):
            count += 1
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    teamA = list(map(int,input().split()))
    teamB = list(map(int,input().split()))
    print(winCountTeamA(teamA,teamB,N)) 
