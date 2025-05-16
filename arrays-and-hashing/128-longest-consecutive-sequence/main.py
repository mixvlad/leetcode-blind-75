from typing import List

def longest_consecutive(nums: List[int]) -> int:
    # Здесь будет ваше решение
    return 0

def main():
    # Тестовые примеры
    test_cases = [
        {
            "nums": [100, 4, 200, 1, 3, 2],
            "expected": 4,
            "name": "Example 1: nums = [100,4,200,1,3,2]"
        },
        {
            "nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
            "expected": 9,
            "name": "Example 2: nums = [0,3,7,2,5,8,4,6,0,1]"
        },
        {
            "nums": [],
            "expected": 0,
            "name": "Example 3: пустой массив"
        },
        {
            "nums": [1],
            "expected": 1,
            "name": "Example 4: один элемент"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = longest_consecutive(tc["nums"])
        status = "✓" if result == tc["expected"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['nums']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 