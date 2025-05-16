from collections import defaultdict
from typing import Dict, List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Используем defaultdict для автоматического создания списков
    groups: Dict[str, List[str]] = defaultdict(list)

    # Группируем строки по подсчету символов
    for s in strs:
        if not s:
            groups["EMPTY"].append(s)
            continue

        # Создаем массив для подсчета символов (26 букв английского алфавита)
        count = [0] * 26
        for c in s:
            # Преобразуем символ в индекс (a=0, b=1, ...)
            count[ord(c) - ord("a")] += 1

        # Преобразуем массив подсчета в строку для использования как ключ
        key = "#".join(map(str, count))
        groups[key].append(s)

    return list(groups.values())


def main():
    # Тестовые примеры
    test_cases = [
        {
            "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            "name": "Example 1: strs = ['eat','tea','tan','ate','nat','bat']",
        },
        {"strs": [""], "expected": [[""]], "name": "Example 2: strs = ['']"},
        {"strs": ["a"], "expected": [["a"]], "name": "Example 3: strs = ['a']"},
        {
            "strs": ["", ""],
            "expected": [["", ""]],
            "name": "Example 4: strs = ['', '']",
        },
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
