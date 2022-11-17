from collections import deque
import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    result=deque()
    N=int(input())
    L=list(map(int, input().split()))
    L.sort()
    result.append(L[0])
    max=0
    for j in range(1,N):
        if j%2==0:
            result.append(L[j])
        else :
            result.appendleft(L[j])
    
    for j in range(N):
        if j == N-1:
            diff=abs(result[N-1]-result[0])
        else:
            diff=abs(result[j]-result[j+1])
        if max<diff:
            max=diff
    print(max)