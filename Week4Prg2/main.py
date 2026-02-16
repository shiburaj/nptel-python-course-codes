# Coder: Shiburaj 

def is_perfect(n):
  divisors=[]
  for x in range(1,n):
    if n%x==0:
      divisors.append(x)
  if sum(divisors)==n:
    return True
  else:
    return False
