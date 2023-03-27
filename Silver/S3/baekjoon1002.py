#식 모름
import math
T=int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    #원의 방정식 (두 원의 거리)
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    #두 원이 동심원이고 반지름이 같을 때
    if distance==0 and r1==r2:
        print(-1)
    #내접, 외접일 때
    elif abs(r1-r2) == distance or r1+r2==distance:
        print(1)
    #두 원이 서로다른 두점에서 만날 때
    elif abs(r1-r2)<distance<(r1+r2):
        print(2)
    else:
        print(0)