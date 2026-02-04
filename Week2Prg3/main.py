params = list(map(int, input().split(" ")))
flag = True
for i in range(0,len(params)-1):
  if params[i] >= params[i+1]:
    flag = False
    break
print(flag, end="")