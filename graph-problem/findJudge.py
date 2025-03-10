# https://leetcode.com/problems/find-the-town-judge/description/
from typing import List


def findJudge(n, trust: List[List[int]]) -> int:
    if (n == 1 and not trust):
        return 1

    trustScore = [0] * (n+1)

    for a, b in trust:
        trustScore[a] -= 1
        trustScore[b] += 1

    for i in range(1, n+1):
        if (trustScore[i] == n-1):
            return i
    return -1


print(findJudge(3, [[1, 2], [1, 3], [2, 3]]))
