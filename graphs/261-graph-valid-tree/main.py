from typing import List
import pytest

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Initialize Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Process all edges
        for u, v in edges:
            # If nodes already have the same parent, adding this edge creates a cycle
            if find(u) == find(v):
                return False
            union(u, v)
        
        # Check if all nodes are in the same set
        # This is actually guaranteed if we have n-1 edges and no cycles
        return True

@pytest.mark.parametrize("n,edges,expected", [
    # Test case 1: Valid tree - simple path
    (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    
    # Test case 2: Invalid tree - contains cycle
    (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    
    # Test case 3: Invalid tree - disconnected components
    (5, [[0, 1], [2, 3]], False),
    
    # Test case 4: Single node tree
    (1, [], True),
    
    # Test case 5: Two node tree
    (2, [[0, 1]], True),
    
    # Test case 6: Invalid tree - too many edges
    (3, [[0, 1], [1, 2], [2, 0]], False),
    
    # Test case 7: Invalid tree - self-loop
    (3, [[0, 1], [1, 1]], False),
])
def test_valid_tree(n, edges, expected):
    """
    Test cases for validating if a graph is a valid tree.
    
    Args:
        n (int): Number of nodes in the graph
        edges (List[List[int]]): List of edges in the graph
        expected (bool): Expected result of validTree function
    """
    solution = Solution()
    assert solution.validTree(n, edges) == expected

if __name__ == "__main__":
    pytest.main([__file__]) 