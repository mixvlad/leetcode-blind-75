from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # 0 = unvisited, 1 = visiting (in current path), 2 = visited
        visited = [0] * numCourses
        
        def dfs(node):
            # If we're revisiting a node in the current path, we found a cycle
            if visited[node] == 1:
                return False
            # If we've already processed this node, skip it
            if visited[node] == 2:
                return True
            
            # Mark as currently visiting
            visited[node] = 1
            
            # Visit all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # Mark as completely visited
            visited[node] = 2
            return True
        
        # Try DFS from each unvisited node
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        
        return True

def main():
    test_cases = [
        {
            "input": [2, [[1, 0]]],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": [2, [[1, 0], [0, 1]]],
            "expected": False,
            "name": "Example 2"
        }
    ]

    solution = Solution()
    for tc in test_cases:
        num_courses = tc["input"][0]
        prerequisites = tc["input"][1]
        result = solution.canFinish(num_courses, prerequisites)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: numCourses = {num_courses}, prerequisites = {prerequisites}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 