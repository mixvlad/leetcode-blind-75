from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pacific_visited, heights[0][c])
            dfs(rows - 1, c, atlantic_visited, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific_visited, heights[r][0])
            dfs(r, cols - 1, atlantic_visited, heights[r][cols - 1])
        
        return list(pacific_visited & atlantic_visited)

def main():
    solution = Solution()
    
    # Test case 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    
    # Test case 2
    heights2 = [[1]]
    
    test_cases = [heights1, heights2]
    
    for i, heights in enumerate(test_cases, 1):
        result = solution.pacificAtlantic(heights)
        print(f"Test case {i}:")
        print(f"Input: {heights}")
        print(f"Result: {result}")
        print()

if __name__ == "__main__":
    main() 