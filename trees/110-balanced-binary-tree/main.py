from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
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
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": [1, 2, 2, 3, 3, None, None, 4, 4],
            "expected": False,
            "name": "Example 2"
        },
        {
            "input": [],
            "expected": True,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        root = list_to_binary_tree(tc["input"])
        result = is_balanced(root)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 