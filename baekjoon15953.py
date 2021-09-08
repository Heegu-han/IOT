T = int(input())

for _ in range(T):
    a, b = map(int, input().split(' '))
    a_prize = 0
    b_prize = 0
    if a == 0:
        a_prize = 0
    elif a == 1:
        a_prize = 500
    elif 2 <= a <= 3:
        a_prize = 300
    elif 4 <= a <= 6:
        a_prize = 200
    elif 7 <= a <= 10:
        a_prize = 50
    elif 11 <= a <= 15:
        a_prize = 30
    elif 16 <= a <= 21:
        a_prize = 10

    if b == 0:
        b_prize = 0
    if b == 1:
        b_prize = 512
    elif 2 <= b <= 3:
        b_prize = 256
    elif 4 <= b <= 7:
        b_prize = 128
    elif 8 <= b <= 15:
        b_prize = 64
    elif 16 <= b <= 31:
        b_prize = 32

    print((a_prize + b_prize) * 10000)
