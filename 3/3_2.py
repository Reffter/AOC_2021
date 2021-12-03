data = [i.strip() for i in open('input').readlines()]

valGamma = []
valEpsilon = []

for column in range(12):
  number0 = 0
  number1 = 0
  for row in range(0, len(data)):
    if(data[row][column] == "0"):
      number0 += 1
    if(data[row][column] == "1"):
      number1 += 1

  if(number0 > number1):
    valGamma.append(0)
    valEpsilon.append(1)
  else:
    valGamma.append(1)
    valEpsilon.append(0)

string_ints = [str(int) for int in valGamma]
gamma = "".join(string_ints)

string_ints = [str(int) for int in valEpsilon]
epsilon = "".join(string_ints)

print(int(gamma, 2)*int(epsilon, 2))