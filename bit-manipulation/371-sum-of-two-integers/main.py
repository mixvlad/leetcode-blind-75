def get_sum(a: int, b: int) -> int:
    # Используем 32-битную маску для работы с отрицательными числами
    mask = 0xFFFFFFFF

    while b != 0:
        # Вычисляем перенос
        carry = (a & b) << 1
        # Вычисляем сумму без учета переноса
        a = (a ^ b) & mask
        # Обновляем b как перенос
        b = carry & mask

    # Если результат отрицательный, преобразуем его
    if a > 0x7FFFFFFF:
        a = ~(a ^ mask)

    return a


def main():
    test_cases = [
        {"input": [1, 2], "expected": 3, "name": "Example 1"},
        {"input": [2, 3], "expected": 5, "name": "Example 2"},
        {"input": [-1, 1], "expected": 0, "name": "Example 3"},
    ]

    for tc in test_cases:
        result = get_sum(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: a = {tc['input'][0]}, b = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
