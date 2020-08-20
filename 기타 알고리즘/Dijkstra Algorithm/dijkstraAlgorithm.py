"""
1. 시작점에서 모든 정점까지의 거리를 담는 배열 (dist) 를 만든다.
2. dist에 시작점을 제외하고, 모두 무한대(inf) 로 설정한다.
3. (시작점, 현재 정점까지의 거리) 을 최소힙에 넣는다. 시작점의 경우 거리는 0이다.
4. 최소힙에서 하나의 정점을 pop한다.
5. 이 정점과 연결된 인접 정점을 adjacent 로 찾는다.
6. (현재 정점까지의 거리 + 현재 정점에서 인접 정점까지의 거리) 와 dist[인접 정점] 거리를 비교하여, 왼쪽이 작을 경우, dist[인접 정점]을 이 값으로 업데이트 한다.
7. 최소힙에 (인접 정점, 인접 정점까지의 거리)를 넣는다.
8. 최소힙이 빌 때까지 4를 반복한다.

다익스트라 알고리즘은 정점을 하나씩 추가하면서 그 때 최적값을 찾아 Relax(더 낮은 거리로 업데이트) 하는 구조다.

출처: https://dailyheumsi.tistory.com/76 [하나씩 점을 찍어 나가며]
"""

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

a = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]

g = Graph()

for i in a:
    g.add_edge(i[0], i[1], i[2])

print(g.dijkstra(1))