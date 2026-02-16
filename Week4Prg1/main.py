# Coder: Shiburaj

def safe_first(L):
  if len(L)==0:
    return None
  else:
    return L[0]
  
def safe_middle(L):
  if len(L)==0:
    return None
  elif len(L)<=2:
    return []
  else:
    del L[0]
    del L[-1]
    return L

def safe_last(L):
  if len(L) ==0:
    return None
  else:
    return L
