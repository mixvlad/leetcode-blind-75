from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [2, [[1, 0]]],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": [2, [[1, 0], [0, 1]]],
            "expected": False,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        num_courses = tc["input"][0]
        prerequisites = tc["input"][1]
        result = can_finish(num_courses, prerequisites)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: numCourses = {num_courses}, prerequisites = {prerequisites}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 