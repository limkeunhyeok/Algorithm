# 알고리즘

## Divide & Conquer

- 주어진 문제를 둘 이상의 부분 문제로 나눈 뒤, 각 문제에 대한 답을 재귀 호출을 통해 계산하고, 각 부분 문제의 답으로부터 전체 문제의 답을 계산하는 방법

![divide](https://user-images.githubusercontent.com/38815618/85421023-e63e4900-b5ae-11ea-943d-e1f7e5e284f1.PNG)

### 분할 정복 알고리즘 구성요소

1. 문제를 더 작은 문제로 분할하는 과정(divide)
2. 각 문제에 대해 구한 답을 원래 문제에 대한 답으로 병합하는 과정(merge)
3. 더이상 답을 분할하지 않고 곧장 풀 수 있는 매우 작은 문제(base case)

### 예제) 쿼드 트리

```python
"""
출처: 알고스팟(https://www.algospot.com/judge/problem/read/QUADTREE)
문제:
쿼드 트리는 2N × 2N 크기의 흑백 그림을 다음과 같은 과정을 거쳐 문자열로 압축합니다.
1. 이 그림의 모든 픽셀이 검은 색일 경우 이 그림의 쿼드 트리 압축 결과는 그림의 크기에 관계없이 b가 됩니다.
2. 이 그림의 모든 픽셀이 흰 색일 경우 이 그림의 쿼드 트리 압축 결과는 그림의 크기에 관계없이 w가 됩니다.
3. 모든 픽셀이 같은 색이 아니라면, 쿼드 트리는 이 그림을 가로 세로로 각각 2등분해 4개의 조각으로 쪼갠 뒤 각각을 쿼드 트리 압축합니다.
 이때 전체 그림의 압축 결과는 x(왼쪽 위 부분의 압축 결과)(오른쪽 위 부분의 압축 결과)(왼쪽 아래 부분의 압축 결과)(오른쪽 아래 부분의 압축 결과)가 됩니다.

쿼드트리로 압축된 흑백그림이 주어졌을 때, 이 그림을 상하로 뒤집은 그림을 쿼드 트리 압축해서 출력하는 프로그램을 작성하세요.

상하좌우 4개로 분할하여 재귀 호출한 뒤, 위치를 바꾸어 합병한다.
"""

# iter() 함수는 전달된 데이터의 반복자를 꺼내 반환한다
def solution(tree):
    return reverse(iter(tree))

# next() 함수는 반복자를 입력받아 그 반복자가 다음에 출력해야 할 요소를 반환한다
def reverse(it):
    current = next(it)
    if current == 'w' or current == 'b':
        return current

    upperLeft = reverse(it)
    upperRight = reverse(it)
    lowerLeft = reverse(it)
    lowerRight = reverse(it)

    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight
```
