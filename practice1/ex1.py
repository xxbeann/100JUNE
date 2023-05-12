p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

pd = {}
pc = {}
answer = []

for i in range(len(p)):
       pd[p[i]] = p.count(p[i])
for k in range(len(c)):
       pc[c[k]] = c.count(c[k])

print(pd)
print(pc)
a = list(pd.keys())
b = list(pc.keys())
print(a)

if len(a) == len(b):
       for j in range(len(a)):
              if pd[a[j]] != pc[a[j]]:
                     answer.append(a[j])

else:
       ans = set(a) - set(b)
       answer = list(ans)

print(answer)
# 아,,,, 모르겠다,,,ㅜㅜ