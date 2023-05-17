a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
temp = []
ans = []
print(c[0][1])

for i in range(len(c)):
    temp = a[c[i][0] - 1:c[i][1]]
    temp.sort()
    ans.append(temp[c[i][2]-1])

print(ans)