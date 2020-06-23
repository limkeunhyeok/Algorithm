# 알고리즘

## Brute Force

- 컴퓨터의 빠른 계산 능력을 이용해 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법

![recursion](https://user-images.githubusercontent.com/38815618/85420932-cf97f200-b5ae-11ea-9201-f2cd03d1f76b.PNG)

### 재귀 호출

- 컴퓨터가 수행하는 많은 작업들은 대개 작은 조각들로 나누어 볼 수 있다
- 들여다보는 범위가 작아질수록 각 조각의 형태가 유사해지는 작업을 많이 볼 수 있다
- 이런 작업에 재귀 호출이 유용하게 사용된다
- 재귀 함수는 자기 자신을 호출하는 함수로, brute force에서는 자신이 수행할 작업을 유사한 형태의 여러 조각으로 쪼갠 뒤 그 중 한 조각을 수행하고, 나머지 조각을 다시 호출하여 사용한다.
- 이때 쪼개지지 않는 가장 작은 작업들을 가리켜 기저 사례(base case)라고 하며, 모든 입력이 기저 사례의 답을 이용해 계산되어야 한다

### 예제) 모든 조합 구하기

```python
"""
배열 arr에서 k개의 원소를 고르는 모든 경우의 수
한 원소를 뽑고, 그 원소를 제외한 배열의 조합을 구한다
comb([1, 2, 3, 4], 2) = ([1] + comb([2, 3, 4], 1)) and
                        ([2] + comb([1, 3, 4], 1)) and
                        ([3] + comb([1, 2, 4], 1)) and
                        ([4] + comb([1, 2, 3], 1))
"""
def comb1(arr, k):
    answer = []
    if k > len(arr):
        return answer

    if k == 1:
        for i in arr:
            answer.append([i])
    else:
        for i in range(len(arr) - k + 1):
            for temp in comb1(arr[i + 1:], k - 1):
                answer.append([arr[i]] + temp)
    return answer

"""
yield는 함수가 제너레이터를 반환한다는 것을 제외하고 return과 비슷하게 사용되는 키워드
제너레이터는 함수가 실행됐는데 더 이상 yield를 만나지 못했을 때 다 끝난 것으로 간주
"""
def comb2(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield arr[i]
        else:
            for j in comb2(arr[i + 1:len(arr)], k - 1):
                yield arr[i] + j
```
