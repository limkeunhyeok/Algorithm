# 알고리즘

## Greedy

- 탐욕법은 각 단계마다 지금 당장 가장 좋은 방법만 선택하는 방법
- 지금의 선택이 앞으로 남은 선택들에 어떤 영향을 끼칠지는 고려하지 않는다
  - 탐욕법은 대부분의 경우 최적해를 찾지 못한다

### 탐욕법이 사용되는 경우

- 탐욕법을 사용해도 항상 최적해를 구할 수 있는 문제를 만난 경우
- 시간이나 공간적 제약으로 인해 다른 방법으로 최적해를 찾기 어려워 근사해 찾는 것으로 타협한 경우

### 정당성 증명

- 탐욕적 선택 속성(greedy choice property)
  - 항상 각 단계에서 선택한 답을 포함하는 최적해가 존재함을 보인다
- 최적 부분 구조(optimal substructure)
  - 각 단계에서 최적의 선택을 했을 때 전체 최적해를 구할 수 있는지 여부를 증명한다

### 탐욕적 알고리즘 레시피

- 문제의 답을 만드는 과정을 여러 조각으로 나눈다
- 각 조각마다 어떤 우선순위로 선택을 내려야 할지 결정한다
- 어떤 방식이 동작할 것 같으면 두 가지 속성을 증명한다

### 예제) 출전 순서 정하기

```python
"""
출처: 알고스팟(https://www.algospot.com/judge/problem/read/MATCHORDER)
문제:
1:1 승부에서는 항상 레이팅이 더 높은 선수가 승리하고, 레이팅이 같을 경우 우리 선수가 승리한다고 가정합시다.
상대방 팀 선수들의 순서를 알고 있을 때, 어느 순서대로 선수들을 내보내야 승수를 최대화할 수 있을까요?

러시아 팀은 내림차순, 한국 팀은 오름차순으로 정렬하고, 러시아팀을 순회하며 한국 팀의 마지막 인덱스와 비교한다
"""

def matchOrder(length, russian, korean):
    answer = 0
    russian = sorted(russian, reverse = True)
    korean = sorted(korean)

    for i in range(length):
        if russian[i] > korean  [-1]:
            continue
        else:
            korean.pop()
            answer += 1
    return answer
```
