def hamming_weight(n: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": 11,  # 00000000000000000000000000001011
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": 128,  # 00000000000000000000000010000000
            "expected": 1,
            "name": "Example 2"
        },
        {
            "input": 4294967293,  # 11111111111111111111111111111101
            "expected": 31,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = hamming_weight(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: n = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 