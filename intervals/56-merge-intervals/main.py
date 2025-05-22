from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        result = []
        current_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                # Merge overlapping intervals
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                # Add non-overlapping interval to result
                result.append(current_interval)
                current_interval = intervals[i]
        
        # Add the last interval
        result.append(current_interval)
        
        return result

def main():
    solution = Solution()
    test_cases = [
        {
            "input": [[1, 3], [2, 6], [8, 10], [15, 18]],
            "expected": [[1, 6], [8, 10], [15, 18]],
            "name": "Example 1"
        },
        {
            "input": [[1, 4], [4, 5]],
            "expected": [[1, 5]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = solution.merge(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 