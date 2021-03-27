# 알고리즘

## Floyd-Warshall

- 최단 경로를 구하는 알고리즘
- 다익스트라 알고리즘은 하나의 정점에서 다른 모든 정점으로의 최단 경로를 구하는 알고리즘이라면, 플로이드-와샬 알고리즘은 모든 정점에서 모든 정점으로 의 최단 경로를 구하는 알고리즘
- 다익스트라 알고리즘은 가장 적은 비용을 하나씩 선택해야 했다면, 플로이드-와샬 알고리즘은 거쳐가는 정점을 기준으로 알고리즘을 수행

### 플로이드-와샬 알고리즘 과정

1. 하나의 정점에서 다른 정점으로 갈 수 있다면 최소 비용, 갈 수 없다면 INF로 배열에 값을 저장한다.
2. 3중 for 문을 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 갱신한다.
3. 위의 과정을 반복해 모든 정점 사이의 최단 경로를 탐색한다.

### 알고리즘 예시

```python
import sys

INF = sys.maxsize

def Floyd_Warshall():
    dist = [[INF] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = a[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = 4
a = [[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]

dist = Floyd_Warshall()

for i in range(n):
    for j in range(n):
        print(dist[i][j], end = ' ')
    print()
```

- 출처 및 참고
    - https://blog.naver.com/ndb796/221234427842
    - https://it-garden.tistory.com/247