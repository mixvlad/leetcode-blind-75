from typing import List


def min_window(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    # Create a dictionary to count the frequency of each character in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Initialize variables for sliding window
    left = 0
    min_len = float("inf")
    min_start = 0
    count = len(t)

    # Iterate through the string with right pointer
    for right in range(len(s)):
        # If current character is in t, decrease its count
        if s[right] in t_count:
            if t_count[s[right]] > 0:
                count -= 1
            t_count[s[right]] -= 1

        # When we have all characters, try to minimize the window
        while count == 0:
            # Update minimum window if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # Try to move left pointer
            if s[left] in t_count:
                t_count[s[left]] += 1
                if t_count[s[left]] > 0:
                    count += 1
            left += 1

    return s[min_start : min_start + min_len] if min_len != float("inf") else ""


def main():
    test_cases = [
        {"input": ["ADOBECODEBANC", "ABC"], "expected": "BANC", "name": "Example 1"},
        {"input": ["a", "a"], "expected": "a", "name": "Example 2"},
        {"input": ["a", "aa"], "expected": "", "name": "Example 3"},
    ]

    for tc in test_cases:
        result = min_window(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input'][0]}, t = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
