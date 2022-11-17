from collections import deque
import sys
import math
input=sys.stdin.readline
N=int(input())
a=list(map(int, input().split()))
result=0
a.sort()
b=deque()
for i in range((N+1)//2):
    b.append(a[i])

for i in b:
    result+=int(math.log2(i))


print(result+1)
