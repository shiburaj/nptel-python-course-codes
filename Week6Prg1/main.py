def multiply(a,b):
  if b == 0:
    return 0
  if b == 1: 
    return a
  else:
    return a + multiply(a,b-1)
