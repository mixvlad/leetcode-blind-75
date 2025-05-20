from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Создаем фиктивный узел
        dummy = ListNode(0)
        dummy.next = head

        # Инициализируем два указателя
        first = dummy
        second = dummy

        # Перемещаем first на n узлов вперед
        for _ in range(n + 1):
            first = first.next

        # Перемещаем оба указателя, пока first не достигнет конца
        while first:
            first = first.next
            second = second.next

        # Удаляем n-й узел с конца
        second.next = second.next.next

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
        {"input": [[1, 2, 3, 4, 5], 2], "expected": [1, 2, 3, 5], "name": "Example 1"},
        {"input": [[1], 1], "expected": [], "name": "Example 2"},
        {"input": [[1, 2], 1], "expected": [1], "name": "Example 3"},
    ]

    for tc in test_cases:
        head = list_to_linked_list(tc["input"][0])
        result = Solution().removeNthFromEnd(head, tc["input"][1])
        result_list = linked_list_to_list(result)
        status = "✓" if result_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: head = {tc['input'][0]}, n = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_list}\n")


if __name__ == "__main__":
    main()
