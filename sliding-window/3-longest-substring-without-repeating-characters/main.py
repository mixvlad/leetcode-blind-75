from collections import deque
from typing import List

def length_of_longest_substring(s: str) -> int:
    max = 0
    queue = deque(maxlen = len(s))
    added_nums = set([])
    for x in s:
        if x in added_nums:
            cur_q_len = len(queue)
            if max < cur_q_len:
                max = cur_q_len
            while True:
                p = queue.popleft()
                added_nums.remove(p)
                if p == x:
                    break
        
        added_nums.add(x)
        queue.append(x)
            
    cur_q_len = len(queue)
    if max < cur_q_len:
        max = cur_q_len
    return max

def main():
    test_cases = [
        {
            "input": "abcabcbb",
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": "bbbbb",
            "expected": 1,
            "name": "Example 2"
        },
        {
            "input": "pwwkew",
            "expected": 3,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = length_of_longest_substring(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 