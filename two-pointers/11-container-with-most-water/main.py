from typing import List

def max_area(height: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
            "name": "Example 1"
        },
        {
            "input": [1, 1],
            "expected": 1,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = max_area(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 