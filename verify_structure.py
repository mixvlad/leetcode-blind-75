import os
import re

def extract_problems_from_readme():
    problems = []
    with open('README.md', 'r') as f:
        content = f.read()
        # Find all problem links in the format [number. Problem Name](path)
        pattern = r'\[(\d+)\.\s+([^\]]+)\]\(([^)]+)\)'
        matches = re.finditer(pattern, content)
        for match in matches:
            number, name, path = match.groups()
            problems.append((number, name, path))
    return problems

def verify_structure():
    problems = extract_problems_from_readme()
    missing = []
    extra = set()
    
    # Get all existing problem directories
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for dir_name in dirs:
            if dir_name not in ['arrays-and-hashing', 'two-pointers', 'sliding-window', 'stack',
                              'binary-search', 'linked-list', 'trees', 'tries', 'heap-priority-queue',
                              'backtracking', 'graphs', 'advanced-graphs', 'dp-1d', 'dp-2d',
                              'greedy', 'intervals', 'math-geometry', 'bit-manipulation']:
                extra.add(os.path.join(root, dir_name))

    # Check each problem from README
    for number, name, path in problems:
        if not os.path.exists(path):
            missing.append((number, name, path))
        else:
            # Remove from extra if it exists
            dir_path = os.path.dirname(path)
            if dir_path in extra:
                extra.remove(dir_path)

    return missing, extra

if __name__ == '__main__':
    missing, extra = verify_structure()
    
    if missing:
        print("\nMissing problem directories:")
        for number, name, path in missing:
            print(f"- {number}. {name} ({path})")
    
    if extra:
        print("\nExtra directories:")
        for path in sorted(extra):
            print(f"- {path}")
    
    if not missing and not extra:
        print("Repository structure matches README.md perfectly!") 