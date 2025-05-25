from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        You are given an array of strings words. Each element of words consists of two lowercase English letters.
        Create the longest possible palindrome by selecting some elements from words and concatenating them in any order.
        Each element can be selected at most once.
        Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

        Time Complexity: O(n), where n is the number of words
        Space Complexity: O(n), where n is the number of words

        Args:
            words: List of two-letter strings

        Returns:
            Length of the longest possible palindrome
        """
        # Count frequency of each word
        word_count = Counter(words)
        length = 0
        has_center = False

        # Process each word
        for word in word_count:
            # Skip if we've already used this word
            if word_count[word] == 0:
                continue

            # If word is a palindrome (e.g., "aa")
            if word[0] == word[1]:
                # We can use pairs of this word
                pairs = word_count[word] // 2
                length += pairs * 4
                # If we have an odd number of this word, we can use one as center
                if word_count[word] % 2 == 1 and not has_center:
                    length += 2
                    has_center = True
            else:
                # For non-palindrome words, find their mirror
                mirror = word[1] + word[0]
                if mirror in word_count:
                    # Use minimum of current word and its mirror
                    pairs = min(word_count[word], word_count[mirror])
                    length += pairs * 4
                    # Mark both words as used
                    word_count[word] -= pairs
                    word_count[mirror] -= pairs

        return length


def main():
    test_cases = [
        {
            "input": ["lc", "cl", "gg"],
            "expected": 6,
            "name": "Example 1 - Basic case"
        },
        {
            "input": ["ab", "ty", "yt", "lc", "cl", "ab"],
            "expected": 8,
            "name": "Example 2 - Multiple pairs"
        },
        {
            "input": ["cc", "ll", "xx"],
            "expected": 2,
            "name": "Example 3 - Single center"
        },
        {
            "input": ["aa", "aa", "aa"],
            "expected": 6,
            "name": "Multiple same palindromes"
        },
        {
            "input": ["ab", "ba", "cd", "dc"],
            "expected": 8,
            "name": "Multiple mirror pairs"
        },
        {
            "input": [],
            "expected": 0,
            "name": "Empty input"
        },
        {
            "input": ["aa"],
            "expected": 2,
            "name": "Single palindrome"
        }
    ]

    solution = Solution()
    for tc in test_cases:
        result = solution.longestPalindrome(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: words = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main() 