from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def main():
    test_cases = [
        {"input": [1, 8, 6, 2, 5, 4, 8, 3, 7], "expected": 49, "name": "Example 1"},
        {"input": [1, 1], "expected": 1, "name": "Example 2"},
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
