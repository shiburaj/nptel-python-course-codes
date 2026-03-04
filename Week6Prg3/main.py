def recursive_min(L):
  if len(L) == 1:
    return L[0]
  last = L.pop()
  if last < L[0]:
    L[0] = last
  return recursive_min(L)
