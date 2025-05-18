from typing import List

def max_profit(prices: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [7, 1, 5, 3, 6, 4],
            "expected": 5,
            "name": "Example 1"
        },
        {
            "input": [7, 6, 4, 3, 1],
            "expected": 0,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = max_profit(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 