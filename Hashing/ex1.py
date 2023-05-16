p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

temp = 0
dic = {}

for part in p:
       dic[hash(part)] = part
       temp += int(hash(part))
for com in c:
       temp -= hash(com)
print(dic)
print(temp)
print(dic[temp])
# 키값이 해쉬함수 value값이 사람이름