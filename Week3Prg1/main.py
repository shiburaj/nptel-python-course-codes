words= input().split(",")

minlen=0
smallest=""
for w in words:
  if minlen==0:
    smallest=w
    minlen=len(w)
  elif len(w)<=minlen:
    smallest = w
    minlen=len(w)
  else:
    pass
  
print(smallest, end="")
    
