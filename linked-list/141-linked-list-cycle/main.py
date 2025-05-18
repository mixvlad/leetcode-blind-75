from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    # TODO: Implement your solution here
    pass

def list_to_linked_list_with_cycle(lst: List[int], pos: int) -> Optional[ListNode]:
    if not lst:
        return None
    
    # Create nodes
    nodes = []
    for val in lst:
        nodes.append(ListNode(val))
    
    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos != -1 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

def main():
    test_cases = [
        {
            "input": [[3, 2, 0, -4], 1],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": [[1, 2], 0],
            "expected": True,
            "name": "Example 2"
        },
        {
            "input": [[1], -1],
            "expected": False,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        head = list_to_linked_list_with_cycle(tc["input"][0], tc["input"][1])
        result = has_cycle(head)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: head = {tc['input'][0]}, pos = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 