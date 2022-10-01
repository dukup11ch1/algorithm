

car_num=int(input())
car_in=[]
car_out=[]
result=0
for i in range(car_num):
    car_in.append(input())
    

for i in range(car_num):
    car_out.append(input())

j=0
for i in range(car_num):
    if car_in[j]==car_out[i]:
        j+=1
    else:
        car_in.remove(car_out[i])
        result+=1

print(result)
"""

7250SI4T 51475H 48642VM F2T56T5K 7JK86BA 03L062 0073MM Y0AD3H K67T3B4 USF316

7250SI4T 0073MM 48642VM F2T56T5K 7JK86BA 03L062 51475H Y0AD3H K67T3B4 USF316
"""