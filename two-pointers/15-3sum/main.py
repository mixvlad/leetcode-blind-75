from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


def main():
    test_cases = [
        {
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]],
            "name": "Example 1",
        },
        {"input": [], "expected": [], "name": "Example 2"},
        {"input": [0], "expected": [], "name": "Example 3"},
    ]

    for tc in test_cases:
        result = three_sum(tc["input"])
        # Sort both result and expected for comparison
        result = sorted([sorted(x) for x in result])
        expected = sorted([sorted(x) for x in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
