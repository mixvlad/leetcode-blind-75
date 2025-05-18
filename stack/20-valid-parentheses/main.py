from typing import List

def is_valid(s: str) -> bool:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "()",
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": "()[]{}",
            "expected": True,
            "name": "Example 2"
        },
        {
            "input": "(]",
            "expected": False,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = is_valid(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 