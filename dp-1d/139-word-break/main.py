from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": ["leetcode", ["leet", "code"]],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": ["applepenapple", ["apple", "pen"]],
            "expected": True,
            "name": "Example 2"
        },
        {
            "input": ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
            "expected": False,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        s = tc["input"][0]
        word_dict = tc["input"][1]
        result = word_break(s, word_dict)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {s}, wordDict = {word_dict}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 