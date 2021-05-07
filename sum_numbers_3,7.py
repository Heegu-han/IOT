total=0

for num in range(1,1001):
    if(num%3)==0 or (num%7)==0:
        total=total+num

print("1부터1000까지 3,7배수의 합은",total,"입니다")
