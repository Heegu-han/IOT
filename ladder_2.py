inp = '''\
a b c d e f
| | | | | |
|-| | |-| |
| | |-| | |
| |-| | |-|
| | |-| | |
|-| | |-| |
| | | | | |
1 2 3 4 5 6'''
board = [i for i in inp.split('\n')]

def ladder(v):
    def check(x,y):
        if y+1<len(board[0]) and board[x][y+1] == '-': return 2
        elif 0<=y-1 and board[x][y-1] == '-':          return -2
        else:                                          return 0

    x,y = 0,board[0].find(v)
    while x < len(board)-1:
        x += 1
        y += check(x,y)
    return board[x][y]


for i in board[0].split(): print(i,ladder(i),sep=' - ')
