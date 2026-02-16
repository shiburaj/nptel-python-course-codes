# Coder : Shiburaj 

def has_duplicates(L):
  d = list(set(L))
  if len(L) == len(d):
    return False
  else:
    return True
