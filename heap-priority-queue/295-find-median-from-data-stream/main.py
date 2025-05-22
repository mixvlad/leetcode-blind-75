import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for lower half (using negative numbers to simulate max heap)
        self.lower_half = []
        # Min heap for upper half
        self.upper_half = []

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.lower_half, -num)
        
        # Balance the heaps
        if self.lower_half and self.upper_half and -self.lower_half[0] > self.upper_half[0]:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)
        
        # Ensure heaps are balanced in size
        if len(self.lower_half) > len(self.upper_half) + 1:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)
        elif len(self.upper_half) > len(self.lower_half):
            val = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -val)

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        return (-self.lower_half[0] + self.upper_half[0]) / 2

def main():
    test_cases = [
        {
            "operations": [
                ("add_num", 1),
                ("add_num", 2),
                ("find_median", 1.5),
                ("add_num", 3),
                ("find_median", 2.0)
            ],
            "name": "Example 1"
        }
    ]

    for tc in test_cases:
        median_finder = MedianFinder()
        print(f"Test Case: {tc['name']}")
        for op in tc["operations"]:
            if op[0] == "add_num":
                median_finder.addNum(op[1])
                print(f"  Added: {op[1]}")
            elif op[0] == "find_median":
                result = median_finder.findMedian()
                expected = op[1]
                status = "✓" if result == expected else "✗"
                print(f"{status} Find Median")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()

if __name__ == "__main__":
    main() 