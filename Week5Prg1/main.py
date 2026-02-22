def divisors(n):
  divs = []
  for i in range(1,n+1):
    if n%i==0:
      divs.append(i)
  return divs

def common_divisors(a,b):
  a_divs = divisors(a)
  b_divs = divisors(b)
  c_divs = []
  for x in a_divs:
    if x in b_divs:
      c_divs.append(x)
      
  return c_divs


def divisors_upto(n):
  dict = {}
  for i in range(1,n+1):
    dict[i] = divisors(i)
  return dict
