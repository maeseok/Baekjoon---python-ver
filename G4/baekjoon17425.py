import sys
N = int(sys.stdin.readline())
for _ in range(N):
    sum=0
    a = int(sys.stdin.readline())
    for i in range(1,a+1):
        sum += (a//i)*i
    print(sum)