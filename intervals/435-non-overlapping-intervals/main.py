from typing import List

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Find the minimum number of intervals to remove to make all intervals non-overlapping.
    
    Args:
        intervals: List of intervals where each interval is [start, end]
        
    Returns:
        int: Minimum number of intervals to remove
    """
    if not intervals:
        return 0
        
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    
    # Keep track of the end of the last selected interval
    last_end = intervals[0][1]
    count = 1  # Count of non-overlapping intervals
    
    # Iterate through remaining intervals
    for start, end in intervals[1:]:
        # If current interval starts after or at the end of last selected interval
        if start >= last_end:
            count += 1
            last_end = end
            
    # Return number of intervals to remove
    return len(intervals) - count

def main():
    test_cases = [
        {
            "input": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1,
            "name": "Example 1"
        },
        {
            "input": [[1, 2], [1, 2], [1, 2]],
            "expected": 2,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = erase_overlap_intervals(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 