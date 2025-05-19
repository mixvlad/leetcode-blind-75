from collections import deque
from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        # Dictionary to count character frequencies in the current window
        char_count = {}
        max_freq = 0  # Maximum frequency of any character in the window
        max_length = 0  # Maximum length of substring
        left = 0  # Left pointer of the window

        # Iterate through the string using right pointer
        for right in range(len(s)):
            # Increment the count for current character
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            # Update maximum frequency
            max_freq = max(max_freq, char_count[s[right]])

            # If number of replacements exceeds k, move left pointer
            while (right - left + 1 - max_freq) > k:
                char_count[s[left]] -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


def main():
    test_cases = [
        {"input": ["ABAB", 2], "expected": 4, "name": "Example 1"},
        {"input": ["AABABBA", 1], "expected": 4, "name": "Example 2"},
        {"input": ["AAAA", 2], "expected": 4, "name": "All same characters"},
        {"input": ["ABCDE", 2], "expected": 3, "name": "All different characters"},
        {"input": ["AABABBA", 2], "expected": 5, "name": "More replacements allowed"},
        {
            "input": [
                "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF",
                4,
            ],
            "expected": 7,
            "name": "Long string with multiple characters",
        },
        {"input": ["", 1], "expected": 0, "name": "Empty string"},
        {"input": ["A", 1], "expected": 1, "name": "Single character"},
        {
            "input": ["ABBB", 2],
            "expected": 4,
            "name": "Wrong Answer Case - Should replace A to get BBBB",
        },
        {
            "input": ["BAAAB", 2],
            "expected": 5,
            "name": "Wrong Answer Case - Should replace B to get AAAAA",
        },
    ]

    solution = Solution()
    for tc in test_cases:
        result = solution.characterReplacement(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input'][0]}, k = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
