import sys

n,m = map(int,input().split())
for i in range(2*n):
    if(i<n):
        list=list(map(str,sys.stdin.readline().split()))
    if(i>=n):
        List =list(map(str,sys.stdin.readline().split()))
print(list,List)

#아직 못 풀음