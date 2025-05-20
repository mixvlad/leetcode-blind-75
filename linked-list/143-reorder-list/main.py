from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # Находим середину списка
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Разворачиваем вторую половину
        prev = None
        curr = slow.next
        slow.next = None  # Разделяем список на две части

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Объединяем две половины
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


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
        {"input": [1, 2, 3, 4], "expected": [1, 4, 2, 3], "name": "Example 1"},
        {"input": [1, 2, 3, 4, 5], "expected": [1, 5, 2, 4, 3], "name": "Example 2"},
    ]

    solution = Solution()
    for tc in test_cases:
        head = list_to_linked_list(tc["input"])
        solution.reorderList(head)
        result_list = linked_list_to_list(head)
        status = "✓" if result_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_list}\n")


if __name__ == "__main__":
    main()
