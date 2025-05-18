from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        @param: n: The number of nodes in the graph
        @param: edges: A list of edges in the graph
        @return: The number of connected components in the graph
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    
    # Test case 2
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    
    test_cases = [(n1, edges1), (n2, edges2)]
    
    for i, (n, edges) in enumerate(test_cases, 1):
        result = solution.countComponents(n, edges)
        print(f"Test case {i}:")
        print(f"Number of nodes: {n}")
        print(f"Edges: {edges}")
        print(f"Number of connected components: {result}")
        print()

if __name__ == "__main__":
    main() 