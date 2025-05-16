def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s1 = {}
    s2 = {}
    for x in s:
        s1[x] = 1 if x not in s1 else s1[x] + 1

    for x in t:
        s2[x] = 1 if x not in s2 else s2[x] + 1

    return s1 == s2


def main():
    # Тестовые примеры
    test_cases = [
        {
            "s": "anagram",
            "t": "nagaram",
            "expected": True,
            "name": "Example 1: s = 'anagram', t = 'nagaram'",
        },
        {
            "s": "rat",
            "t": "car",
            "expected": False,
            "name": "Example 2: s = 'rat', t = 'car'",
        },
        {"s": "", "t": "", "expected": True, "name": "Example 3: пустые строки"},
        {
            "s": "hello",
            "t": "world",
            "expected": False,
            "name": "Example 4: разные слова",
        },
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
