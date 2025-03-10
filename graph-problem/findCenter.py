# https://leetcode.com/problems/find-center-of-star-graph/description/
from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if not edges:
            return -1

        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]


graphProblem = Solution()

print(graphProblem.findCenter([]))

print(graphProblem.findCenter([[1, 2], [2, 3], [4, 2]]))

print(graphProblem.findCenter([[1, 2], [2, 3], [4, 3]]))
