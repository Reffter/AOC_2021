data = [int(i.strip()) for i in open('input').readlines()]
count = 0

for i in range(0, len(data)-1):
  v1 = data[i]
  v2 = data[i+1]
  if v2 > v1:
    count += 1

print(count)