class MedianFinder:
    def __init__(self):
        # TODO: Initialize your data structure here
        pass

    def add_num(self, num: int) -> None:
        # TODO: Implement your solution here
        pass

    def find_median(self) -> float:
        # TODO: Implement your solution here
        pass

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
                median_finder.add_num(op[1])
                print(f"  Added: {op[1]}")
            elif op[0] == "find_median":
                result = median_finder.find_median()
                expected = op[1]
                status = "✓" if result == expected else "✗"
                print(f"{status} Find Median")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()

if __name__ == "__main__":
    main() 