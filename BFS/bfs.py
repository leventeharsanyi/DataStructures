from collections import deque

class Node:
    def __init__(self, value, children=None):
        if children is None:
            children = []
        self.value = value
        self.children = children

def bfs(root, target) -> bool:
    queue = deque([root])
    visited = {root}
    while queue:
        node = queue.popleft()
        for child in node.children:
            if child in visited:
                continue
            if child.value == target:
                return True
            queue.append(child)
            visited.add(child)
    return False

if __name__ == "__main__":
    print(bfs(Node(1, [Node(2), Node(3)]),3))