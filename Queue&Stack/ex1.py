a = [4, 4, 4, 3, 3]
ans = []
for i in range(len(a)-1):
    if(a[i] != a[i+1]):
        ans.append(a[i])
ans.append(a[-1])
print(ans)