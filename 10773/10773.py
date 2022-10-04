class stack:
    def __init__(self):
        self.a=[]
        self.len=0
    def push(self,data):
        self.a.append(data)
        self.len+=1
    def pop(self):
        self.len-=1
        re=self.a[self.len]
        del self.a[self.len]
        return re
    def sum(self):
        ssum=0
        for i in self.a:
            ssum+=i
        return ssum


k=int(input())
result=stack()
for i in range(k):
    n=input()
    if n != "0":
        result.push(int(n))
    else :
        result.pop()

print(result.sum())