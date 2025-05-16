from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Здесь будет ваше решение
    return []

def main():
    # Тестовые примеры
    test_cases = [
        {
            "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            "name": "Example 1: strs = ['eat','tea','tan','ate','nat','bat']"
        },
        {
            "strs": [""],
            "expected": [[""]],
            "name": "Example 2: strs = ['']"
        },
        {
            "strs": ["a"],
            "expected": [["a"]],
            "name": "Example 3: strs = ['a']"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = group_anagrams(tc["strs"])
        # Сортируем внутренние списки и сам результат для стабильного сравнения
        result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(group) for group in tc["expected"]])
        status = "✓" if result == expected else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: strs = {tc['strs']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 