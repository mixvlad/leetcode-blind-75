from collections import deque
from typing import List

def is_valid(s: str) -> bool:
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = deque()
    for i in s:
        if i in open_par:
            stack.append(i)
        elif not stack or i != bracket_map[stack.pop()]:
            return False
    return not stack

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