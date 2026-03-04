def digit_sum(n):
  last = n%10
  rem = n // 10
  if rem == 0:
    return last
  return last + digit_sum(rem)
