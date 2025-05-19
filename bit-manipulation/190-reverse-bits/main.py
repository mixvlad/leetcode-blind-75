def reverse_bits(n: int) -> int:
    n = (n >> 16) | (n << 16)
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    return n


def main():
    test_cases = [
        {
            "input": 43261596,  # 00000010100101000001111010011100
            "expected": 964176192,  # 00111001011110000010100101000000
            "name": "Example 1",
        },
        {
            "input": 4294967293,  # 11111111111111111111111111111101
            "expected": 3221225471,  # 10111111111111111111111111111111
            "name": "Example 2",
        },
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
