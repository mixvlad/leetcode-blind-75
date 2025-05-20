from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True

            # Check if the node value is within the valid range
            if (left is not None and node.val <= left) or (
                right is not None and node.val >= right
            ):
                return False

            # Recursively check left and right subtrees
            # For left subtree: all values must be less than current node
            # For right subtree: all values must be greater than current node
            return validate(node.left, left, node.val) and validate(
                node.right, node.val, right
            )

        return validate(root, None, None)


def print_tree(node, prefix="", is_left=True):
    if not node:
        return

    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
    print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
    print_tree(node.right, prefix + ("    " if is_left else "│   "), False)


def run_test(solution, root, expected, test_name):
    result = solution.isValidBST(root)
    print(f"\nТест: {test_name}")
    print("-" * 50)

    if root:
        print("Структура дерева:")
        print_tree(root)
    else:
        print("Пустое дерево")

    print(f"\nОжидаемый результат: {'✓ Валидное' if expected else '✗ Невалидное'} BST")
    print(f"Полученный результат: {'✓ Валидное' if result else '✗ Невалидное'} BST")

    if result == expected:
        print("✓ Тест пройден успешно")
    else:
        print("✗ Тест не пройден!")
        print(f"Ошибка: алгоритм вернул {result}, ожидалось {expected}")

    print("=" * 50)
    return result == expected


def main():
    solution = Solution()
    tests_passed = 0
    total_tests = 0

    print("=" * 50)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА ВАЛИДАЦИИ BST")
    print("=" * 50)

    # Test case 1: Пустое дерево (должно быть валидным)
    root1 = None
    total_tests += 1
    if run_test(solution, root1, True, "Пустое дерево"):
        tests_passed += 1

    # Test case 2: Дерево с одним узлом (должно быть валидным)
    root2 = TreeNode(1)
    total_tests += 1
    if run_test(solution, root2, True, "Дерево с одним узлом"):
        tests_passed += 1

    # Test case 3: Простое валидное BST
    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    root3.right = TreeNode(3)
    total_tests += 1
    if run_test(solution, root3, True, "Простое валидное BST"):
        tests_passed += 1

    # Test case 4: Невалидное BST
    root4 = TreeNode(5)
    root4.left = TreeNode(1)
    root4.right = TreeNode(4)
    root4.right.left = TreeNode(3)
    root4.right.right = TreeNode(6)
    total_tests += 1
    if run_test(solution, root4, False, "Невалидное BST"):
        tests_passed += 1

    # Test case 5: BST с отрицательными значениями
    root5 = TreeNode(-10)
    root5.left = TreeNode(-15)
    root5.right = TreeNode(-5)
    total_tests += 1
    if run_test(solution, root5, True, "BST с отрицательными значениями"):
        tests_passed += 1

    # Test case 6: Дерево с дубликатами (должно быть невалидным)
    root6 = TreeNode(1)
    root6.left = TreeNode(1)
    total_tests += 1
    if run_test(solution, root6, False, "BST с дубликатами"):
        tests_passed += 1

    # Test case 7: Сложное валидное BST
    root7 = TreeNode(8)
    root7.left = TreeNode(3)
    root7.right = TreeNode(10)
    root7.left.left = TreeNode(1)
    root7.left.right = TreeNode(6)
    root7.left.right.left = TreeNode(4)
    root7.left.right.right = TreeNode(7)
    root7.right.right = TreeNode(14)
    root7.right.right.left = TreeNode(13)
    total_tests += 1
    if run_test(solution, root7, True, "Сложное валидное BST"):
        tests_passed += 1

    # Test case 8: Невалидное BST с отрицательными значениями [0,null,-1]
    root8 = TreeNode(0)
    root8.right = TreeNode(-1)
    total_tests += 1
    if run_test(solution, root8, False, "Невалидное BST с отрицательными значениями"):
        tests_passed += 1

    print("\nИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Пройдено тестов: {tests_passed} из {total_tests}")
    print(f"Успешность: {(tests_passed/total_tests)*100:.1f}%")


if __name__ == "__main__":
    main()
