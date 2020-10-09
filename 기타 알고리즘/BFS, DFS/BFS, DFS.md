# 알고리즘

- 그래프 탐색이란 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것

## BFS(너비 우선 탐색, Breadth-First Search)

![1](https://user-images.githubusercontent.com/38815618/95591801-bf832000-0a82-11eb-9f26-c654ffb7b7ba.PNG)

- 루트 노드에서 시작해 인접한 노드를 먼저 탐색하는 방법
- 시작에서 가까운 노드를 먼저 방문하고 멀리 떨어져 있는 노드는 나중에 방문하는 순회 방법
- 깊게보단 넓게 탐색하는 방법
- 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 사용
- 큐를 이용해서 구현
- 인접 리스트로 표현된 그래프: O(N+E)
- 인접 행렬로 표현된 그래프: O(N^2)
- 노드의 개수에 비해 엣지 개수가 적은 경우 인접 리스트를 사용하는 것이 효율적

## DFS(깊이 우선 탐색, Depth-First Search)

![2](https://user-images.githubusercontent.com/38815618/95591806-c0b44d00-0a82-11eb-88d8-af3cba5d49ac.PNG)

- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 넓게보단 깊게 탐색하는 방법
- 모든 노드를 방문 하고자 하는 경우에 사용
- 스택을 이용해서 구현
- 인접 리스트로 표현된 그래프: O(N+E)
- 인접 행렬로 표현된 그래프: O(N^2)
- 노드의 개수에 비해 엣지 개수가 적은 경우 인접 리스트를 사용하는 것이 효율적

### 출처 및 참고

- https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html
- https://sinsomi.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Python-BFS-DFS-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%EC%B4%88%EC%BD%94%EB%8D%94
