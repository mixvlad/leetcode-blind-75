def is_anagram(s: str, t: str) -> bool:
    # Здесь будет ваше решение
    return False

def main():
    # Тестовые примеры
    test_cases = [
        {
            "s": "anagram",
            "t": "nagaram",
            "expected": True,
            "name": "Example 1: s = 'anagram', t = 'nagaram'"
        },
        {
            "s": "rat",
            "t": "car",
            "expected": False,
            "name": "Example 2: s = 'rat', t = 'car'"
        },
        {
            "s": "",
            "t": "",
            "expected": True,
            "name": "Example 3: пустые строки"
        },
        {
            "s": "hello",
            "t": "world",
            "expected": False,
            "name": "Example 4: разные слова"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = is_anagram(tc["s"], tc["t"])
        status = "✓" if result == tc["expected"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: s = '{tc['s']}', t = '{tc['t']}'")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 