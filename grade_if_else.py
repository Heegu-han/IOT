score=int(input("총점을 입력하세요."))

if score>=90:
    print("a")
else:
    if 80<=score<90:
        print("b")
    else:
        if 70<=score<80:
            print("c")
        else:
            if 60<=score<70:
                print("d")
            else:
                print("f")
