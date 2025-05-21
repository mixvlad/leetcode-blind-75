def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring using Manacher's algorithm.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
    
    # Преобразуем строку, добавляя разделители
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    
    # Массив для хранения радиусов палиндромов
    p = [0] * n
    
    # Центр и правая граница текущего палиндрома
    center = right = 0
    
    # Начало и длина самой длинной палиндромной подстроки
    max_start = max_len = 0
    
    for i in range(n):
        if i < right:
            # Используем симметрию для инициализации
            p[i] = min(right - i, p[2 * center - i])
        
        # Расширяем палиндром в обе стороны
        left = i - (p[i] + 1)
        right_expand = i + (p[i] + 1)
        
        while left >= 0 and right_expand < n and t[left] == t[right_expand]:
            p[i] += 1
            left -= 1
            right_expand += 1
        
        # Обновляем центр и правую границу
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        # Обновляем максимальную длину
        if p[i] > max_len:
            max_len = p[i]
            max_start = (i - max_len) // 2
    
    return s[max_start:max_start + max_len]

def main():
    test_cases = [
        {
            "input": "babad",
            "expected": "bab",
            "name": "Example 1"
        },
        {
            "input": "cbbd",
            "expected": "bb",
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = longest_palindrome(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 