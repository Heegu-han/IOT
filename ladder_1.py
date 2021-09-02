inp = '''a b c d e f
| | | | | |
|-| | |-| |
| | |-| | |
| |-| | |-|
| | |-| | |
|-| | |-| |
| | | | | |
1 2 3 4 5 6
'''

a, *b, c = inp.splitlines()
c = list(c)
for line in b:
  for i, x in enumerate(line):
    if i % 2 == 1 and x == '-':
      c[i-1], c[i+1] = c[i+1], c[i-1]

result = list(zip(a, c))[::2]
for x, y in result:
  print(f'{x} - {y}')
