def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


def main():
    test_cases = [
        {"input": 2, "expected": 2, "name": "Example 1"},
        {"input": 3, "expected": 3, "name": "Example 2"},
    ]

    for tc in test_cases:
        result = climb_stairs(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: n = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
