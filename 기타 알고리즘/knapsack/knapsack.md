# 알고리즘

## Knapsack

> 배낭 문제(Knapsack Problem)은 조합 최적화 문제 중 하나로, 배낭에 담을 수 있는 무게의 최댓값이 정해져 있으며 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때, 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제이다.

- 배낭 문제는 짐을 쪼갤 수 있는 경우(분할가능 배낭문제, Fractional Knapsack Problem), 짐을 쪼갤 수 없는 경우 (0-1 배낭문제, 0-1 Knapsack Problem)로 나뉜다.

### 풀이

- Brute Force를 적용하면, 최악의 경우 O(2^n)이기 때문에 매우 느리다.
- Greedy를 적용하면, 최적의 답을 보장하지 못한다.(Fractional Knapsack Problem의 경우, greedy로 풀 수 있음)
- Dynamic Programming을 적용하려면 최적의 원리(Principle of Optimality)가 성립하는지 확인해야 한다.
  - 어떤 문제의 입력 사례의 최적해가 그 입력 사례를 분할한 부분 사례에 대한 최적해를 항상 포함하고 있으면, 그 문제에 대하여 최적의 원리가 성립한다.
  - 집합 A를 n개의 보석들 중에 최적으로 고른 부분 집합이라고 가정할 때,
    - 집합 A가 n번째 보석을 포함하고 있지 않다면, A는 n번째 보석을 뺀 나머지 n-1개의 보석들 중에서 최적으로 고른 부분집합과 같다.
    - 집합 A가 n번째 보석을 포함하고 있다면, A에 속한 보석들의 총 가격은 n-1개의 보석들 중에서 최적으로 고른 가격의 합에다가 보석 n의 가격을 더한 것과 같다. (단, n번째 보석을 넣었을 때 배낭이 터지지 않아야 한다)

### 사용 예시

- 배에 컨테이너를 실을 때, 균형과 무게의 조화가 필요
- 천을 재단할 때, 낭비되는 천의 부분을 최소화
- 강의실 편성할 때, 고려조건은 수강인원과 강의실 수용 인원
- 자원이 일정할 때, 그 자원을 어디에 배치시킬 것인지 결정한다.
