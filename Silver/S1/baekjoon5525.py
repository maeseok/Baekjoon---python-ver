n=int(input())
m=int(input())
s=input()
tmp="IO"*n+'I'
a=len(tmp)
ans,i,cnt=0,0,0
while i<m-1:
    if s[i:i+3]=='IOI':
        i+=2
        cnt+=1
        if cnt==n:
            ans+=1
            cnt-=1
    else:
        i+=1
        cnt=0
print(ans)