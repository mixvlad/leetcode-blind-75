from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Проверяем, находится ли левая половина в отсортированном порядке
        if nums[left] <= nums[mid]:
            # Если целевое значение находится в левой половине
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Если целевое значение находится в правой половине
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def main():
    test_cases = [
        {"input": [[4, 5, 6, 7, 0, 1, 2], 0], "expected": 4, "name": "Example 1"},
        {"input": [[4, 5, 6, 7, 0, 1, 2], 3], "expected": -1, "name": "Example 2"},
        {"input": [[1], 0], "expected": -1, "name": "Example 3"},
    ]

    for tc in test_cases:
        result = search(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input'][0]}, target = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
