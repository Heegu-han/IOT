age = int(input("나이를 입력하시오:"))
height=int(input("키를 입력하시오:"))

if age >= 40:
    if height<=170:
        print("큽니다.")
    else:
        print("보통입니다.")
else:
    if height >= 175:
        print("큽니다.")
    else:
        print("보통입니다.")
