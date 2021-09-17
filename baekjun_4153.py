while True:
  s1, s2, s3 = map(int, input().split())
  if s1==0:
    break
  if max(s1,s2,s3)==s1:
    if s1**2==s2**2 + s3**2:
      print("right")
    else:
      print("wrong")
  elif max(s1,s2,s3)==s2:
    if s2**2==s1**2 + s3**2:
      print("right")
    else:
      print("wrong")
  elif max(s1,s2,s3)==s3:
    if s3**2==s2**2 + s1**2:
      print("right")
    else:
      print("wrong")
