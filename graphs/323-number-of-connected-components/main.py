from typing import List
import pytest

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize DSU
        parent = list(range(n))
        rank = [0] * n
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return
                
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        # Process all edges
        for x, y in edges:
            union(x, y)
        
        # Count unique roots
        return len(set(find(x) for x in range(n)))

def test_count_components():
    solution = Solution()
    
    # Test case 1: Two separate components
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    assert solution.countComponents(n1, edges1) == 2
    
    # Test case 2: One connected component
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert solution.countComponents(n2, edges2) == 1
    
    # Test case 3: No edges
    n3 = 4
    edges3 = []
    assert solution.countComponents(n3, edges3) == 4
    
    # Test case 4: Single node
    n4 = 1
    edges4 = []
    assert solution.countComponents(n4, edges4) == 1
    
    # Test case 5: Multiple separate components
    n5 = 6
    edges5 = [[0, 1], [2, 3], [4, 5]]
    assert solution.countComponents(n5, edges5) == 3

if __name__ == "__main__":
    pytest.main([__file__]) 