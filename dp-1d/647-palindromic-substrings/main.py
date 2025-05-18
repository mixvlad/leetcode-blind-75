def count_substrings(s: str) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "abc",
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": "aaa",
            "expected": 6,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = count_substrings(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 