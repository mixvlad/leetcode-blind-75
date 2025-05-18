from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        @param: n: The number of nodes in the graph
        @param: edges: A list of edges in the graph
        @return: True if the graph is a valid tree, False otherwise
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1: Valid tree
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    
    # Test case 2: Invalid tree (has cycle)
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    
    # Test case 3: Invalid tree (disconnected)
    n3 = 5
    edges3 = [[0, 1], [2, 3]]
    
    test_cases = [(n1, edges1), (n2, edges2), (n3, edges3)]
    
    for i, (n, edges) in enumerate(test_cases, 1):
        result = solution.validTree(n, edges)
        print(f"Test case {i}:")
        print(f"Number of nodes: {n}")
        print(f"Edges: {edges}")
        print(f"Is valid tree: {result}")
        print()

if __name__ == "__main__":
    main() 