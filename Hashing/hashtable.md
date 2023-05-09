
# Hashtable study
---
프로그래머스 완주하지 못한 선수 문제를 풀다 오류가 생겨따

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