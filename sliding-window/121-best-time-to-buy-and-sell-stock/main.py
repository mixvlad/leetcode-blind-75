from typing import List
import sys
def max_profit(prices: List[int]) -> int:
    maxsell = 0
    minbuy = sys.maxsize
    for x in prices:
        diff = x - minbuy
        if x < minbuy:
            minbuy = x
        elif diff > maxsell:
            maxsell = diff
    return maxsell

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