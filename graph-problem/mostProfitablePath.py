# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
from typing import List
from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        blob_times = {}
        maxProfit = float('-inf')

        # Bob Path Tracking
        def dfs(src, parent, time):
            if (src == 0):
                blob_times[src] = time
                return True

            for neighbour in graph[src]:
                if (neighbour == parent):
                    continue
                if dfs(neighbour, src, time+1):
                    blob_times[src] = time
                    return True

            return False

        dfs(bob, -1, 0)

        queue = deque([[0, 0, -1, amount[0]]])  # node,time,parent,profit
        maxProfit = float('-inf')

        while queue:
            node, time, parent, profit = queue.popleft()

            for neighbour in graph[node]:
                if (neighbour == parent):
                    continue
                neighbourProfit = amount[neighbour]
                neighbourTime = time + 1
                # Check Blob ever visited that neighbour node. If yes then check time
                if neighbour in blob_times:
                    # If Blob reached the first compare to Alice then Alice-'s Time > Blob's Time And Alice will have zero profit
                    if (neighbourTime > blob_times[neighbour]):
                        neighbourProfit = 0
                    if (neighbourTime == blob_times[neighbour]):
                        # Both reachs at same time
                        neighbourProfit = amount[neighbour] // 2

                queue.append((neighbour, neighbourTime,
                              node, neighbourProfit + profit))

                # Check neighbour node has leaf node then update max-profit
                if (len(graph[neighbour]) == 1):
                    maxProfit = max(maxProfit, neighbourProfit + profit)

        return maxProfit


graphProblem = Solution()

print(graphProblem.mostProfitablePath(
    [[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]))

print(graphProblem.mostProfitablePath(
    [[0, 1]], 1, [-7280, 2350]))
