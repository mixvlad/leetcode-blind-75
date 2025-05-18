from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
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

def binary_tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

def main():
    test_cases = [
        {
            "input": [4, 2, 7, 1, 3, 6, 9],
            "expected": [4, 7, 2, 9, 6, 3, 1],
            "name": "Example 1"
        },
        {
            "input": [2, 1, 3],
            "expected": [2, 3, 1],
            "name": "Example 2"
        },
        {
            "input": [],
            "expected": [],
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        root = list_to_binary_tree(tc["input"])
        result = invert_tree(root)
        result_list = binary_tree_to_list(result)
        status = "✓" if result_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_list}\n")

if __name__ == "__main__":
    main() 