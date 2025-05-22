from typing import List
import unittest

class Solution:
    """
    Solution for the Insert Interval problem.
    Given a set of non-overlapping intervals, insert a new interval into the intervals.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert a new interval into a list of non-overlapping intervals.
        
        Args:
            intervals: List of non-overlapping intervals
            newInterval: New interval to insert
            
        Returns:
            List of intervals after insertion
        """
        result = []
        i = 0
        
        # Add all intervals that end before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Merge all overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Add the merged interval
        result.append(newInterval)
        
        # Add all remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
            
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_insert(self):
        test_cases = [
            {
                "intervals": [[1, 3], [6, 9]],
                "newInterval": [2, 5],
                "expected": [[1, 5], [6, 9]],
                "name": "Example 1"
            },
            {
                "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                "newInterval": [4, 8],
                "expected": [[1, 2], [3, 10], [12, 16]],
                "name": "Example 2"
            },
            {
                "intervals": [],
                "newInterval": [5, 7],
                "expected": [[5, 7]],
                "name": "Empty intervals"
            },
            {
                "intervals": [[1, 5]],
                "newInterval": [2, 3],
                "expected": [[1, 5]],
                "name": "New interval inside existing"
            },
            {
                "intervals": [[1, 5]],
                "newInterval": [6, 8],
                "expected": [[1, 5], [6, 8]],
                "name": "New interval after existing"
            },
            {
                "intervals": [[1, 5]],
                "newInterval": [0, 0],
                "expected": [[0, 0], [1, 5]],
                "name": "New interval before existing"
            },
            {
                "intervals": [[1, 5], [6, 8]],
                "newInterval": [5, 6],
                "expected": [[1, 8]],
                "name": "New interval connects two existing"
            },
            {
                "intervals": [[1, 5], [6, 8], [9, 10]],
                "newInterval": [4, 9],
                "expected": [[1, 10]],
                "name": "New interval overlaps multiple intervals"
            }
        ]
        
        for tc in test_cases:
            with self.subTest(tc["name"]):
                result = self.solution.insert(tc["intervals"], tc["newInterval"])
                self.assertEqual(result, tc["expected"])

if __name__ == "__main__":
    unittest.main() 