from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s == "":
                res += "ъй"
            else:
                res += s + "эв"
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str: str) -> List[str]:
        res = []
        i = 0
        while i < len(str) - 1:
            j = i
            if str[j] == "ъ" and str[j + 1] == "й":
                res.append("")
            else:
                while str[j] != "э" and str[j + 1] != "в":
                    j += 1
                res.append(str[i:j])
            i = j + 2
        return res


def main():
    solution = Solution()

    # Тестовые примеры
    test_cases = [
        {"strs": ["hello", "world"], "name": "Example 1: strs = ['hello', 'world']"},
        {"strs": [""], "name": "Example 2: strs = ['']"},
        {"strs": ["a", "b", "c"], "name": "Example 3: strs = ['a', 'b', 'c']"},
        {"strs": ["lint;:;:;", "code", "love", "you"], "name": "Example 4"},
        {
            "strs": ["hello", "", "world"],
            "name": "Example 4: strs = ['hello', '', 'world']",
        },
    ]

    # Запуск всех тестов
    for tc in test_cases:
        # Кодируем строки
        encoded = solution.encode(tc["strs"])
        # Декодируем обратно
        decoded = solution.decode(encoded)

        status = "✓" if decoded == tc["strs"] else "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: strs = {tc['strs']}")
        print(f"  Encoded: {encoded}")
        print(f"  Decoded: {decoded}\n")


if __name__ == "__main__":
    main()
