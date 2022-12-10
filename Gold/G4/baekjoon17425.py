import sys
input=sys.stdin.readline
tmp=[]
for i in range(int(input())):
    tmp.append(int(input().rstrip()))
n=max(tmp)
arr=[False,False]+([True]*(int(n**0.5)+1))
for i in range(2,int(n**0.5)+1):
    if i*i>int(n**0.5):
        break
    for j in range(2*i,int(n**0.5)+1,i):
        arr[j]=False