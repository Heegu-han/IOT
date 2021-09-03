    line = int(input("Tree 의 높이를 입력하세요(5~30) : "))

    for x in range(1, line * 2, 2):
        print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

    for y in range(1, 4):
        print(" " * (line-2) + "***")
