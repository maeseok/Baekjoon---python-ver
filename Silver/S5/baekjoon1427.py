n=input()
arr=[]
for i in range(len(n)):
    arr.append(n[i])
arr.sort(reverse=True)
answer=""
for j in arr:
    answer+=j
print(int(answer))