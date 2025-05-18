from typing import List

def count_bits(n: int) -> List[int]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": 2,
            "expected": [0, 1, 1],
            "name": "Example 1"
        },
        {
            "input": 5,
            "expected": [0, 1, 1, 2, 1, 2],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = count_bits(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: n = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 