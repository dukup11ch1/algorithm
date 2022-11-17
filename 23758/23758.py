import sys
import math
input=sys.stdin.readline
N=int(input())
a=list(map(int, input().split()))
result=0
a.sort()
a=a[:(N+1)//2]


for i in a:
    result+=int(math.log2(i))


print(result+1)
