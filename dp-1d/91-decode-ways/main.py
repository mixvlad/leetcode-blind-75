def num_decodings(s: str) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "12",
            "expected": 2,
            "name": "Example 1"
        },
        {
            "input": "226",
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = num_decodings(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 