from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    h = {}
    for x in nums:
        h[x] = 1 if x not in h else h[x] + 1
    return any(v > 1 for k, v in h.items())


def main():
    # Тестовые примеры
    test_cases = [
        {"nums": [1, 2, 3, 1], "expected": True, "name": "Example 1: nums = [1,2,3,1]"},
        {
            "nums": [1, 2, 3, 4],
            "expected": False,
            "name": "Example 2: nums = [1,2,3,4]",
        },
        {
            "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True,
            "name": "Example 3: nums = [1,1,1,3,3,4,3,2,4,2]",
        },
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = contains_duplicate(tc["nums"])
        status = "✓" if result == tc["expected"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['nums']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
