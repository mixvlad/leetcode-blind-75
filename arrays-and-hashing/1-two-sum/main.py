from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # Создаем хеш-таблицу для хранения чисел и их индексов
    num_map = {}
    
    # Проходим по массиву один раз
    for i, num in enumerate(nums):
        # Вычисляем число, которое нам нужно найти
        complement = target - num
        
        # Если это число уже есть в хеш-таблице, значит мы нашли пару
        if complement in num_map:
            return [num_map[complement], i]
        
        # Добавляем текущее число и его индекс в хеш-таблицу
        num_map[num] = i
    
    # Если решение не найдено (хотя по условию задачи оно всегда существует)
    return []

def main():
    # Тестовые примеры из условия задачи
    test_cases = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
            "name": "Example 1: nums = [2,7,11,15], target = 9"
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
            "name": "Example 2: nums = [3,2,4], target = 6"
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1],
            "name": "Example 3: nums = [3,3], target = 6"
        }
    ]

    # Запуск всех тестов
    for tc in test_cases:
        result = two_sum(tc["nums"], tc["target"])
        status = "✓"

        # Проверка результата (порядок индексов может быть любым)
        if len(result) != len(tc["expected"]):
            status = "✗"
        else:
            # Проверяем валидность результата
            valid = False
            if (len(result) == 2 and result[0] != result[1] and
                result[0] >= 0 and result[0] < len(tc["nums"]) and
                result[1] >= 0 and result[1] < len(tc["nums"]) and
                tc["nums"][result[0]] + tc["nums"][result[1]] == tc["target"]):
                valid = True
            if not valid:
                status = "✗"

        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['nums']}, target = {tc['target']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 