def common_elements(L1, L2):
  Com = []
  for x in L1:
    if x in L2 and x not in Com:
      Com.append(x)
      
  return Com
