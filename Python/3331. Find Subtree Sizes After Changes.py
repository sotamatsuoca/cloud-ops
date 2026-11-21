class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        stacks = [[] for _ in range(26)]
        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()
            c = ord(s[node]) - 97
            if state == 0:
                if stacks[c]:
                    new_parent[node] = stacks[c][-1]
                stacks[c].append(node)
                stack.append((node, 1))
                for child in children[node]:
                    stack.append((child, 0))
            else:
                stacks[c].pop()

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n
        order = []
        todo = [0]
        while todo:
            node = todo.pop()
            order.append(node)
            for child in new_children[node]:
                todo.append(child)

        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer