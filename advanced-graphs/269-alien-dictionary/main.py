from typing import List

def alien_order(words: List[str]) -> str:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": ["wrt", "wrf", "er", "ett", "rftt"],
            "expected": "wertf",
            "name": "Example 1"
        },
        {
            "input": ["z", "x"],
            "expected": "zx",
            "name": "Example 2"
        },
        {
            "input": ["z", "x", "z"],
            "expected": "",
            "name": "Example 3 (cycle)"
        }
    ]

    for tc in test_cases:
        result = alien_order(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: words = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 