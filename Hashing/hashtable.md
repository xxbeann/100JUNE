
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
<br>그럼 이 문제를 해결하기 위해서는 어떻게 해야 할까요?
<br>그러게 말입니다. 열심히 생각중이에요 딕셔너리를 이용하래요 딕셔너리를 한번 공부해보겠습니다.
