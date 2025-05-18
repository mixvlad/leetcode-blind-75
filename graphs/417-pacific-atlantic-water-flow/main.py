from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        @param: heights: A 2D integer array representing the height of each cell
        @return: A list of coordinates where water can flow to both the Pacific and Atlantic oceans
        """
        pass

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