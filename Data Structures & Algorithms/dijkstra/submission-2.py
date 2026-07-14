class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(n)}
        dist[src] = 0
        visited = set()
        p = [(0, src)]

        while p:
            d, u = heapq.heappop(p)
            if u in visited:
                continue
            visited.add(u)

            for v, w in graph[u]:
                if v in visited:
                    continue
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(p, (nd, v))

        return {k: (v if v != float('inf') else -1) for k, v in dist.items()}