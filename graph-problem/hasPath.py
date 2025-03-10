# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
from collections import deque, defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        if not edges:
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False  # Already at the end, so no need for extra `return False`


graphProblem = Solution()

print(graphProblem.validPath(1, [], 0, 0))

print(graphProblem.validPath(2, [], 0, 1))

print(graphProblem.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 0))

print(graphProblem.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))

print(graphProblem.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 5))
