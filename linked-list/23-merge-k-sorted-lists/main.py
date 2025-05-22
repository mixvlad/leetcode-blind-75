import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    # Create a min-heap to store the smallest elements
    min_heap = []

    # Initialize the heap with the first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    # Create a dummy head for the merged list
    dummy = ListNode()
    current = dummy

    # Process until the heap is empty
    while min_heap:
        # Pop the smallest element from the heap
        val, i, node = heapq.heappop(min_heap)

        # Add the node to the merged list
        current.next = node
        current = current.next

        # If there is a next node, push it to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next


def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def main():
    test_cases = [
        {
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6],
            "name": "Example 1",
        },
        {"input": [], "expected": [], "name": "Example 2"},
        {"input": [[]], "expected": [], "name": "Example 3"},
    ]

    for tc in test_cases:
        lists = [list_to_linked_list(lst) for lst in tc["input"]]
        result = merge_k_lists(lists)
        result_list = linked_list_to_list(result)
        status = "✓" if result_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_list}\n")


if __name__ == "__main__":
    main()
