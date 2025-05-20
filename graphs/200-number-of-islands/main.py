from copy import deepcopy
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def zero(i, j):
            if i != m and i != -1 and j != n and j != -1 and grid[i][j] == "1":
                grid[i][j] = "0"
                zero(i + 1, j)
                zero(i - 1, j)
                zero(i, j + 1)
                zero(i, j - 1)
            return

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    total += 1
                    zero(i, j)

        return total


def main():
    solution = Solution()
    test_cases = [
        {
            "input": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected": 1,
            "name": "Example 1",
        },
        {
            "input": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            "expected": 3,
            "name": "Example 2",
        },
        {
            "input": [
                ["1", "1", "1"],
                ["0", "1", "0"],
                ["1", "1", "1"],
            ],
            "expected": 1,
            "name": "Example 3 - Complex Island",
        },
        {
            "input": [
                ["1", "0", "1", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["1", "0", "1", "0", "1"],
            ],
            "expected": 8,
            "name": "Example 4 - Multiple Small Islands",
        },
    ]

    for tc in test_cases:
        # Create a deep copy of the input grid for each test
        grid_copy = deepcopy(tc["input"])
        result = solution.numIslands(grid_copy)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: grid = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
