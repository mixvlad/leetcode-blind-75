from typing import List

def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [2, [[1, 0]]],
            "expected": [0, 1],
            "name": "Example 1"
        },
        {
            "input": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
            "expected": [[0, 2, 1, 3], [0, 1, 2, 3]],  # Both are valid
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        num_courses = tc["input"][0]
        prerequisites = tc["input"][1]
        result = find_order(num_courses, prerequisites)
        # For Example 2, check if result is one of the valid outputs
        if isinstance(tc["expected"], list) and any(isinstance(e, list) for e in tc["expected"]):
            status = "✓" if result in tc["expected"] else "✗"
        else:
            status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: numCourses = {num_courses}, prerequisites = {prerequisites}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 