import sys
input=sys.stdin.readline
fibo=[0,1]
for i in range(50):
    fibo.append(fibo[i]+fibo[i+1])
del fibo[0]
fibo.sort(reverse=True)

T=int(input())
for i in range(T):
    n=int(input())
    result=[]
    for j in fibo:
        if n>=j:
            result.append(j)
            n=n-j
    result.sort()
    for j in result:
        print(j,end=' ')
    print("\n",end="")