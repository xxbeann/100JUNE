f = open("C:/Users/y_jeo/Desktop/strace.txt", 'rt', encoding='UTF-8')
# line = f.readline()
# print(line)
list = []

for line in f:
  each = line.split()
  if len(each) < 3: continue
  target = each[2]
  for i in range(len(target)):
    p = -1
    if target[i] == '(':
      p = i
      break
  list.append(target[:p])
  print(target[:p])
print(set(list))