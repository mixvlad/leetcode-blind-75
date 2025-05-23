from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def main():
    test_cases = [
        {"input": [[0, 30], [5, 10], [15, 20]], "expected": False, "name": "Example 1"},
        {"input": [[7, 10], [2, 4]], "expected": True, "name": "Example 2"},
    ]

    for tc in test_cases:
        result = can_attend_meetings(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
