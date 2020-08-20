# 알고리즘

## Dijkstra Algorithm

<p>
    그래프에서 정점끼리의 최단 경로를 구하는 문제는 여러가지 방법이 있다.
</p>

- 하나의 정점에서 다른 정점까지의 최단 경로를 구하는 문제(single source and single destination shortest path problem)
- 하나의 정점에서 다른 모든 정점까지의 최단 경로를 구하는 문제(single source shortest path problem)
- 하나의 목적지로 가는 최단 경로를 구하는 문제(single destination shortest path problem)
- 마지막으로 모든 최단 경로를 구하는 문제(all pairs shortest path problem)

<p>
    다익스트라 알고리즘은 2번째 방법으로 간선들은 모두 양의 간선들을 가져야 한다. 기본 로직은 첫 정점을 기준으로 연결되어 있는 정점들을 추가해가며, 최단 거리를 갱신하는 것이다. 정점을 잇기 전까지는 시작점을 제외한 정점들은 모두 무한대 값을 가진다.
</p>

### 다익스트라 알고리즘 예시

![1](https://user-images.githubusercontent.com/38815618/90789788-4698ff00-e342-11ea-81a7-e269f2bd905b.PNG)

1. 먼저 시작점(A)의 최단 거리 값을 0으로 두고 나머지 모든 버텍스의 최단 거리값을 Infinity(무한)으로 설정한다.
2. A와 연결된 B, C의 거리 값을 조정하는데, 시작점 거리 값에 아크 값을 더한 것보다 도착점 거리 값이 크면 도착점 거리 값을 더한 값으로 낮춘다.
    - 시작점 거리 값(A, 0)에 아크 값(6)을 더한 것(0+6)보다 도착점 거리 값(B, 무한)이 크면 도착점 거리 값을 더한 값(6)으로 바꾼다.
3. A, B, C를 구한 상태에서 B를 기준으로 반복하고, C를 기준으로 반복하여 거리 값을 갱신한다.
4. 무한 값이 없어질 때까지 반복한다.

<p>
    다익스트라 알고리즘은 앞서 언급한대로 양의 값을 가져야 하며, 음의 값을 가진 경우 다른 알고리즘(벨만-포드)을 사용해야 한다.
</p>

```py
from collections import defaultdict
import heapq

class Graph():
    def __init__(self):
        self.edges = defaultdict(dict)

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight

    def dijkstra(self, start):
        min_heap = []
        dist = { v: float('inf') for v in self.edges.keys() }

        heapq.heappush(min_heap, (0, start))
        dist[start] = 0

        while min_heap:
            current_dist, current_v = heapq.heappop(min_heap)

            for next_v, next_dist in self.edges[current_v].items():
                total_dist = current_dist + next_dist

                if total_dist < dist[next_v]:
                    dist[next_v] = total_dist
                    heapq.heappush(min_heap, (total_dist, next_v))

        return dist
```

- 출처 및 참고
  - https://www.zerocho.com/category/Algorithm/post/584bd46f580277001862f1af
  - https://hsp1116.tistory.com/42
  - https://dailyheumsi.tistory.com/76