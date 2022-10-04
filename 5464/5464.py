
class parking:
    def __init__(self,fee):
        self.fee=fee
        self.carnum=None
        self.tf=False

park=[]
cars={}
que=[]
carsum=0
result=0
N,M=list(map(int, input().split(" ")))

for i in range(N):
    park.append(parking(int(input())))
parknum=len(park)

for i in range(M):
    cars[i+1]=int(input())

for i in range(M*2):
    a=input()
    if a[0]=="-":
        for j in park:
            if j.carnum == int(a[1:]):
                j.tf = False
                j.carnum=None
                carsum-=1
                break
    else:
        que.append(int(a))
    if que.__len__() != 0:
        if carsum<parknum:
            carsum+=1
            for j in park:
                if j.tf is False:
                    j.tf = True
                    j.carnum = que[0]
                    result+=j.fee*cars[j.carnum]
                    del que[0]
                    break

print(result)