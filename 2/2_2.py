data = [i.strip() for i in open('input').readlines()]

X = 0
Y = 0
aim = 0

for row in data:
  whereTo = row.split()[0]
  howMuch = int(row.split()[1])
  if(whereTo == "forward"):
    X += howMuch
    Y += (aim*howMuch)
  if(whereTo == "down"):
    aim += howMuch
  if(whereTo == "up"):
    aim -= howMuch

print(X*Y)