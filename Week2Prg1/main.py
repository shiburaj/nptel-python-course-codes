
l = list(map(int, input().split(" ")))

avg = sum(l)/len(l)
count = 0
for d in l:
  if d > avg:
    count += 1
    
print(count, end="")
