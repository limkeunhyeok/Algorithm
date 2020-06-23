# 알고리즘

## Dynamic Programming

- 동적 계획법은 큰 의미에서는 분할 정복과 같은 접근 방식을 취한다
- 여러번 중복되는 부분 문제의 계산 결과를 저장하고 결과를 재활용하여 속도의 향상을 꾀할 수 있다

![subproblem](https://user-images.githubusercontent.com/38815618/85421061-f2c2a180-b5ae-11ea-944b-fdc1da7074fc.PNG)

### 메모이제이션(Memoization)

- 함수의 결과를 저장하는 장소를 마련해 두고 한 번 계산한 값을 저장해 뒀다 재활용하는 최적화 기법
- 메모이제이션 기법을 적용하려면 호출하고자 하는 함수가 참조적 투명성(referential transparency)를 가져야 한다

### 예제) 타일링

```python
"""
출처: 알고스팟(https://www.algospot.com/judge/problem/read/TILING2)
문제: 2xn 크기의 사각형을 2x1 크기의 사각형으로 빈틈없이 채우는 경우의 수를 구하는 프로그램을 작성하세요.

맨 왼쪽이 어떻게 채워져 있는냐로 분류하여 점화식을 세우면
tiling(n) = tiling(n - 1) + tiling(n - 2)
"""

def tiling(n):
    dp = [1, 2]
    if n == 1: return dp[0]
    if n == 2: return dp[1]
    for i in range(n - 2):
        dp.append(dp[i] + dp[i + 1])
    return dp[-1] % 1000000007
```
