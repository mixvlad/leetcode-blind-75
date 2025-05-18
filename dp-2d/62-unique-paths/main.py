def unique_paths(m: int, n: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [3, 7],
            "expected": 28,
            "name": "Example 1"
        },
        {
            "input": [3, 2],
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        m = tc["input"][0]
        n = tc["input"][1]
        result = unique_paths(m, n)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: m = {m}, n = {n}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 