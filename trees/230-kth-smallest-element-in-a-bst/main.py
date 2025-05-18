from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    # TODO: Implement your solution here
    pass

def list_to_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def main():
    test_cases = [
        {
            "input": [[3, 1, 4, None, 2], 1],
            "expected": 1,
            "name": "Example 1"
        },
        {
            "input": [[5, 3, 6, 2, 4, None, None, 1], 3],
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        root = list_to_binary_tree(tc["input"][0])
        k = tc["input"][1]
        result = kth_smallest(root, k)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: root = {tc['input'][0]}, k = {k}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 