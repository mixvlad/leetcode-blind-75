from typing import List

def min_window(s: str, t: str) -> str:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": ["ADOBECODEBANC", "ABC"],
            "expected": "BANC",
            "name": "Example 1"
        },
        {
            "input": ["a", "a"],
            "expected": "a",
            "name": "Example 2"
        },
        {
            "input": ["a", "aa"],
            "expected": "",
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = min_window(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input'][0]}, t = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 