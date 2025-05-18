def reverse_bits(n: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": 43261596,  # 00000010100101000001111010011100
            "expected": 964176192,  # 00111001011110000010100101000000
            "name": "Example 1"
        },
        {
            "input": 4294967293,  # 11111111111111111111111111111101
            "expected": 3221225471,  # 10111111111111111111111111111111
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = reverse_bits(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: n = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 