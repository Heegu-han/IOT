N = int(input())
arr=[]
maxnum=N//3

for i in range(maxnum+1):
    if (N-i*3)/5 == int((N-i*3)/5):
        if N==i*3:    
            arr.append(int(i))
        else:
            arr.append(int(i+(N-i*3)/5))

if len(arr)==0:
    print('-1')
else:
    print(min(arr))
