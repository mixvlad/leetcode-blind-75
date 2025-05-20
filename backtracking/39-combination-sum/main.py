from functools import lru_cache
from typing import List

import pytest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates for optimization
        candidates.sort()

        # Early termination if smallest number is greater than target
        if not candidates or candidates[0] > target:
            return []

        # Calculate minimum possible length of combination
        min_length = (target + candidates[-1] - 1) // candidates[-1]
        # Calculate maximum possible length of combination
        max_length = target // candidates[0]

        if min_length > max_length:
            return []

        res = []
        # Convert candidates to tuple for caching
        candidates_tuple = tuple(candidates)

        @lru_cache(maxsize=None)
        def dfs(target, index, path):
            if target == 0:
                res.append(list(path))
                return
            if target < candidates_tuple[index]:
                return
            for i in range(index, len(candidates_tuple)):
                if candidates_tuple[i] > target:
                    break
                dfs(target - candidates_tuple[i], i, path + (candidates_tuple[i],))

        dfs(target, 0, ())
        return res


def test_combination_sum():
    """
    Test cases for combinationSum function
    """
    solution = Solution()

    # Test case 1: Basic case
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    result1 = solution.combinationSum(candidates1, target1)
    assert sorted([sorted(comb) for comb in result1]) == sorted(
        [sorted(comb) for comb in expected1]
    )

    # Test case 2: Empty result
    candidates2 = [2, 4, 6]
    target2 = 1
    expected2 = []
    result2 = solution.combinationSum(candidates2, target2)
    assert result2 == expected2

    # Test case 3: Single number
    candidates3 = [1]
    target3 = 2
    expected3 = [[1, 1]]
    result3 = solution.combinationSum(candidates3, target3)
    assert sorted([sorted(comb) for comb in result3]) == sorted(
        [sorted(comb) for comb in expected3]
    )

    # Test case 4: Large target
    candidates4 = [2, 3, 5]
    target4 = 8
    expected4 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result4 = solution.combinationSum(candidates4, target4)
    assert sorted([sorted(comb) for comb in result4]) == sorted(
        [sorted(comb) for comb in expected4]
    )

    # Test case 5: Impossible case due to length constraints
    candidates5 = [4, 5, 6]
    target5 = 7
    expected5 = []
    result5 = solution.combinationSum(candidates5, target5)
    assert result5 == expected5


if __name__ == "__main__":
    pytest.main([__file__])
