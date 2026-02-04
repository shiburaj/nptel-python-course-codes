temps = map(int, input().split(" "))
danger = []
for t in temps:
  if t > 50:
    danger.append(str(t))

if len(danger) == 0:
  print("0", end="")
else:
  print(" ".join(danger), end="")