import sys
import math
input=sys.stdin.readline
from collections import deque
T=int(input())
for _ in range(T):
    num_slime=int(input())
    slime=list(map(int, input().split()))
    slime.sort()
    result=1
    for i in range(len(slime)):
        if len(slime)==1:
            break
        result*=slime[0]*slime[1]
        slime.append(slime[0]*slime[1])
        del slime[0]
        del slime[0]
        slime.sort()
    print(result%1000000007)
