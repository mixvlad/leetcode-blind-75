from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Здесь будет ваше решение
    return []

def main():
    # Тестовые примеры
    test_cases = [
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
            "name": "Example 1: nums = [1,1,1,2,2,3], k = 2"
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1],
            "name": "Example 2: nums = [1], k = 1"
        },
        {
            "nums": [1, 2, 3, 4, 5, 1, 2, 3, 1, 2],
            "k": 3,
            "expected": [1, 2, 3],
            "name": "Example 3: nums = [1,2,3,4,5,1,2,3,1,2], k = 3"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = top_k_frequent(tc["nums"], tc["k"])
        # Сортируем результат для стабильного сравнения
        result.sort()
        expected = sorted(tc["expected"])
        status = "✓" if result == expected else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['nums']}, k = {tc['k']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 