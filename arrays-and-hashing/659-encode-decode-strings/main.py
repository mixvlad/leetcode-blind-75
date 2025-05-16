from typing import List

def encode(strs: List[str]) -> str:
    # Здесь будет ваше решение
    return ""

def decode(s: str) -> List[str]:
    # Здесь будет ваше решение
    return []

def main():
    # Тестовые примеры
    test_cases = [
        {
            "strs": ["hello", "world"],
            "name": "Example 1: strs = ['hello', 'world']"
        },
        {
            "strs": [""],
            "name": "Example 2: strs = ['']"
        },
        {
            "strs": ["a", "b", "c"],
            "name": "Example 3: strs = ['a', 'b', 'c']"
        },
        {
            "strs": ["hello", "", "world"],
            "name": "Example 4: strs = ['hello', '', 'world']"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        # Кодируем строки
        encoded = encode(tc["strs"])
        # Декодируем обратно
        decoded = decode(encoded)
        
        status = "✓" if decoded == tc["strs"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: strs = {tc['strs']}")
        print(f"  Encoded: {encoded}")
        print(f"  Decoded: {decoded}\n")

if __name__ == "__main__":
    main() 