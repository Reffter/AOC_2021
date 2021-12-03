data = [int(i.strip()) for i in open('input').readlines()]
inc = 0
old = -1
s = []

for i in range(0, len(data)-2):
  s.append(data[i] + data[i+1] + data[i+2])

for i in range(0, len(s)-1):
  if s[i+1] > s[i]:
    old = s[i+1]
    inc += 1

print(inc)