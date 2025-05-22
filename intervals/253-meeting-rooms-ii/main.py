from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # Initialize min heap with end time of first meeting
        min_heap = [intervals[0].end]
        
        # Process remaining meetings
        for i in range(1, len(intervals)):
            # If current meeting starts after the earliest ending meeting,
            # we can reuse that room
            if intervals[i].start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            # Add current meeting's end time to heap
            heapq.heappush(min_heap, intervals[i].end)
        
        return len(min_heap)

def main():
    solution = Solution()
    test_cases = [
        {
            "input": [Interval(0, 30), Interval(5, 10), Interval(15, 20)],
            "expected": 2,
            "name": "Example 1"
        },
        {
            "input": [Interval(7, 10), Interval(2, 4)],
            "expected": 1,
            "name": "Example 2"
        },
        {
            "input": [Interval(0, 30), Interval(5, 10), Interval(15, 20), 
                     Interval(25, 35), Interval(30, 40)],
            "expected": 2,
            "name": "Multiple overlapping meetings"
        },
        {
            "input": [Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(4, 5)],
            "expected": 1,
            "name": "Consecutive non-overlapping meetings"
        },
        {
            "input": [Interval(0, 1), Interval(0, 1), Interval(0, 1), Interval(0, 1)],
            "expected": 4,
            "name": "All meetings at same time"
        },
        {
            "input": [Interval(1, 10), Interval(2, 7), Interval(3, 19), 
                     Interval(8, 12), Interval(10, 20), Interval(11, 30)],
            "expected": 4,
            "name": "Complex overlapping pattern"
        },
        {
            "input": [],
            "expected": 0,
            "name": "Empty intervals"
        },
        {
            "input": [Interval(1, 1)],
            "expected": 1,
            "name": "Single zero-duration meeting"
        }
    ]

    for tc in test_cases:
        result = solution.minMeetingRooms(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {[(i.start, i.end) for i in tc['input']]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 