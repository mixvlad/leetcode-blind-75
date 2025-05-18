class WordDictionary:
    def __init__(self):
        # TODO: Initialize your data structure here
        pass

    def add_word(self, word: str) -> None:
        # TODO: Implement your solution here
        pass

    def search(self, word: str) -> bool:
        # TODO: Implement your solution here
        pass

def main():
    test_cases = [
        {
            "operations": [
                ("add_word", "bad"),
                ("add_word", "dad"),
                ("add_word", "mad"),
                ("search", "pad", False),
                ("search", "bad", True),
                ("search", ".ad", True),
                ("search", "b..", True)
            ],
            "name": "Example 1"
        }
    ]

    for tc in test_cases:
        wd = WordDictionary()
        print(f"Test Case: {tc['name']}")
        for op in tc["operations"]:
            if op[0] == "add_word":
                wd.add_word(op[1])
                print(f"  Added: {op[1]}")
            elif op[0] == "search":
                result = wd.search(op[1])
                expected = op[2]
                status = "✓" if result == expected else "✗"
                print(f"{status} Search: {op[1]}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()

if __name__ == "__main__":
    main() 