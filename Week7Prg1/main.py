def unique_elements(L):
  uni = []
  for x in L:
    if x not in uni:
      uni.append(x)
      
  return uni
