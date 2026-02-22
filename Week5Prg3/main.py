def char_frequency(s):
  dict = {}
  sep = list(s)
  for x in sep:
    if dict.get(x) == None:
      dict[x] = 1
    else:
      dict[x] += 1
      
  return dict
