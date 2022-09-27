# BFS

import collections


def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    parent = {0: -1}
    queue = collections.deque([0])

    while queue:
        node = queue.popleft()

        for neighbour in adj_list[node]:

            # Don't look at the trivial cycle.
            if neighbour == parent[node]:
                continue

            # Check if we've already seen this node.
            if neighbour in parent:
                return False

            # Otherwise, put this neighbour onto queue and record that it has been seen.
            parent[neighbour] = node
            queue.append(neighbour)

    return len(parent) == n
