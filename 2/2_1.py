data = [i.strip() for i in open('input').readlines()]

X = 0
Y = 0

for row in data:
  whereTo = row.split()[0]
  howMuch = int(row.split()[1])
  if(whereTo == "forward"):
    X += howMuch
  if(whereTo == "down"):
    Y += howMuch
  if(whereTo == "up"):
    Y -= howMuch

print(X*Y)