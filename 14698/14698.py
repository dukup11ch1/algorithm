import sys
import math
input=sys.stdin.readline
from collections import deque

N,w=list(map(int, input().split()))
big_candy=[]
small_candy=[]
for _ in range(N):
    t,s=tuple(map(int, input().split()))
    if t==5:
        big_candy.append(s)
    else :
        small_candy.append(s)

big_candy.sort(reverse=True)
small_candy.sort(reverse=True)

next_big=[0]
for i in range(len(big_candy)):
    next_big.append(next_big[i]+big_candy[i])

next_small=[0]
for i in range(len(small_candy)):
    next_small.append(next_small[i]+small_candy[i])

big_num=min(w//5,len(big_candy))
result=0
while big_num >= 0:
    small_num = min(int((w-big_num*5)/3), len(small_candy))
    result = max(result, next_big[big_num] + next_small[small_num])
    big_num -= 1
print(result)