# 알고리즘

## Binary Search

- 이진 탐색 알고리즘(Binary Search Algorithm)은 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.
- 정렬된 리스트의 중간 값을 선택해, 그 값과 대소를 비교하여 위치를 찾는다.
- 시간복잡도는 logN이다.

### 예시

- 오름차순으로 정렬된 중복되지 않은 배열 arr이 있다. 이 수열에서 value의 위치를 찾는 프로그램을 작성하시오.

![1](https://user-images.githubusercontent.com/38815618/110745609-dcfd2580-827e-11eb-9794-b7558cb0907b.PNG)

- start는 0, end는 배열의 마지막 인덱스이며, mid는 start와 end의 중간에 위치하는 인덱스이다.
- 매 mid에 위치하는 값과 value를 비교한다.
  - mid에 위치하는 값과 value가 같다면, mid를 반환한다.
  - mid에 위치하는 값보다 value가 작다면, end에 mid 값을 할당하고 다시 mid 값을 계산한다.
  - mid에 위치하는 값과 value가 크다면, start에 mid 값을 할당하고 다시 mid 값을 계산한다.

## Upper/Lower Bound

- Upper/Lower Bound는 이진 탐색을 활용한 알고리즘이다.
- 정렬된 리스트에서 찾고자 하는 Key 값이 있을 때, Upper Bound는 Key보다 큰 첫번째 위치(초과)를 반환하고, Lower Bound는 Key보다 크거나 같은 첫번째 위치(이상)를 반환한다.
- 리스트 [1, 3, 3, 5, 7]이 있을 때
  - key = 3이면 Upper Bound = 3(인덱스), Lower Bound = 1(인덱스)이다.
  - key = 2이면 Upper Bound = 1(인덱스), Lower Bound = 1(인덱스)가 된다.
