
# Hashtable study
프로그래머스 완주하지 못한 선수(42576) 문제를 풀다 오류가 생겨따<br>
문제에 관한 자세한 내용은 프로그래머스를 참조하기 바랍니다.

정리를 하자면 참가자와 완주자가 있는데 완주하지 못한 사람을 구하면 됩니다.
<br> 참가자는 완주자보다 한 명 더 많고 동명이인이 있을 수 있습니다.

```python
def solution(participant, completion):
    answer = []
    # 동명이인이 없는 경우
    p = set(participant)
    c = set(completion)
    answer = list(p - c)
    # 동명이인이 있는 경우
    if len(answer) == 0:
        participant.sort()
        for i in range(len(participant) - 2):
            if (participant[i] == participant[i + 1]):
                answer.append(participant[i])
    return answer[0]
```
다음과 같이 코드를 작성했으나 오류가 있었습니다.<br>
동명이인이 없는 경우는 간단하게 집합으로 변환해서 차집합을 구해주면 완주하지 못한 사람이 간단하게 나오게 됩니다.
<br>그러나 문제는 동명이인이 있을 경우 발생하게 됩니다.
<br>제가 작성한 코드는 동명이인이 참가자에 1쌍 있을 경우입니다.(예 "aladin", "aladin", "bank", "comedy")
<br>(참가자리스트를 정렬하여 양쪽으로 반복되는 이름이 있을 경우 그 이름을 리턴)
<br>그래서 동명이인이 3명 이상일 경우에는 오류가 발생하죠
<br>즉, 최초풀이에서 참가자와 완주자의 자료형을 set으로 바꾼뒤 차를 구해 해가 있을 경우 값을 리턴, 값이 없을 경우 동명이인중 한 명을 출력하는 풀이를 생각하고 있었습니다.
<br>하지만 이 풀이로는 동명이인 중 누가 완주하지 못했는지 찾아내는게 불가능합니다.<strong>애초에 케이스를 저렇게 나누면 안댔다,,,</strong>
<br>그럼 이 문제를 해결하기 위해서는 어떻게 해야 할까요?
<br>그러게 말입니다. 열심히 생각중이에요 딕셔너리를 이용하래요 딕셔너리를 한번 공부해보겠습니다.
```python
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
```
다음과 같이 코드를 짜봤는데 역시 풀리지 않습니다. 시간복잡도에서 오류가나더군요,,,
<br>사람이름과 사람이름이 나오는 횟수를 딕셔너리로 이용해서 사랑 이름이 나오는 횟수가 변하면 완주하지 못한사람으로 간주하기로했는데,,,안나오네요  😞
```python
temp = 0
dic = {}

for part in p:
       dic[hash(part)] = part
       temp += int(hash(part))
for com in c:
       temp -= hash(com)
```
결국 구글링을 통해 다음과 같이 해결했네여,,,(어렵,,,,)
<br>key값이 해쉬함수 value값을 사람 이름으로해서 매핑시켜줬습니다.
<br>여기서 필요한 생각은 언제 적재적소에 해쉬함수를 이용해서 문제를 해결해 나가느냐 인것같은데...
<br>이 부분은 좀 더 시간이 필요할 것 같습니다,,,아직 감이 안잡혀요,,,
