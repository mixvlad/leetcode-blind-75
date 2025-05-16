from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    # Здесь будет ваше решение
    return []

def main():
    # Тестовые примеры
    test_cases = [
        {
            "nums": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6],
            "name": "Example 1: nums = [1,2,3,4]"
        },
        {
            "nums": [-1, 1, 0, -3, 3],
            "expected": [0, 0, 9, 0, 0],
            "name": "Example 2: nums = [-1,1,0,-3,3]"
        },
        {
            "nums": [2, 3],
            "expected": [3, 2],
            "name": "Example 3: nums = [2,3]"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = product_except_self(tc["nums"])
        status = "✓" if result == tc["expected"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['nums']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 