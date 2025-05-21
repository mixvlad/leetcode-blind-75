class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings using Manacher's algorithm.
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            s (str): Input string
            
        Returns:
            int: Number of palindromic substrings
        """
        # Преобразуем строку, добавляя разделители
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n  # массив радиусов палиндромов
        center = right = 0
        count = 0
        
        for i in range(1, n - 1):
            # Используем симметрию для инициализации p[i]
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            
            # Расширяем палиндром
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            # Обновляем center и right если нужно
            if i + p[i] > right:
                center, right = i, i + p[i]
            
            # Подсчитываем палиндромы
            count += (p[i] + 1) // 2
        
        return count

def main():
    solution = Solution()
    test_cases = [
        {
            "input": "abc",
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": "aaa",
            "expected": 6,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = solution.countSubstrings(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 