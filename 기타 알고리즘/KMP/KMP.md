# 알고리즘

## KMP

- 문자열 검색 알고리즘으로 KMP는 만든 사람의 앞글자이다.
- 시간 복잡도는 O(N + M)으로 Brute Force O(NM)보다 매우 빠르다.
- KMP 알고리즘을 이해하기 위해선 2가지를 알아두어야 한다.

### 접두사(prefix)와 접미사(suffix)

- banana로 예를 들면

|접두사|접미사|
|---|---|
|b|a|
|ba|na|
|ban|ana|
|bana|nana|
|banan|anana|
|banana|banana|

### pi 배열

- pi[i]는 주어진 문자열의 0 ~ i 까지의 부분 문자열 중에서 prefix == suffix가 될 수 있는 부분 문자열중 가장 긴 것의 길이이다.

![pi배열](https://user-images.githubusercontent.com/38815618/86530570-afdcc400-bef4-11ea-8804-aa0b34d5f97e.PNG)

### 원리

![kmp원리](https://user-images.githubusercontent.com/38815618/86530569-aeab9700-bef4-11ea-970c-f83d60009ce4.PNG)

- kmp 알고리즘은 틀렸다는 사실이 아니라 조금이라도 일치했었다는 정보에 주목하고, 미리 전처리 해둔 pi 배열을 이용해서 많은 중간 시도를 건너뛸 수 있게 한다.