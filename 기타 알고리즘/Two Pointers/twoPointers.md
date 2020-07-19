# 알고리즘

## Two Pointers Algorithm

- 1차원 배열이 있고 이 배열에서 각자 다른 원소를 가리키고 있는 2개의 포인터를 조작해 문제를 해결하는 알고리즘이다.
- 이 알고리즘은 직관적으로 O(n^2) 이상으로 해결해야 하는 문제를 선형시간O(n)으로 해결해준다.
- sliding window는 2개의 포인터를 사용한다는 점에서 비슷하나, 포인터 간의 구간이 일정한 크기를 유지한다는 점에서 다르다.

### 예제) 수들의 합

- N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
  - N개의 원소를 가진 배열에서 부분 배열의 합이 M이 되는 횟수를 구하는 문제
- 배열이 [1,2, 3, 4, 2, 5, 3, 1, 1, 2]이고, 합이 5

![1](https://user-images.githubusercontent.com/38815618/87878562-fca9ba00-ca1f-11ea-83f6-35a920764498.PNG)

- 여기서 빨간색 포인터가 start, 파란색 포인터가 end이고, S는 두 포인터 사이 부분 배열의 합이다.
- 여기서 S < M일 경우 파란색 포인터를 증가시키고, S >= M일 경우 빨간색 포인터를 증가시킨다.

![2](https://user-images.githubusercontent.com/38815618/87878564-fd425080-ca1f-11ea-919d-a2e96e78c9fa.PNG)
![3](https://user-images.githubusercontent.com/38815618/87878565-fddae700-ca1f-11ea-884a-237d5eabb5ce.PNG)
![4](https://user-images.githubusercontent.com/38815618/87878566-fddae700-ca1f-11ea-88f7-f85c00e47591.PNG)
![5](https://user-images.githubusercontent.com/38815618/87878567-fe737d80-ca1f-11ea-9b81-b432decf6358.PNG)
![6](https://user-images.githubusercontent.com/38815618/87878569-fe737d80-ca1f-11ea-86b3-6d0354264a86.PNG)

- 해당 알고리즘은 매 루프마다 항상 두 포인터 중 하나는 1씩 증가하고 있고, 각 포인터가 N번 누적 증가해야 알고리즘이 종료된다.
  - 각각의 포인터가 배열 끝에 다다르는데 O(N)이다.
