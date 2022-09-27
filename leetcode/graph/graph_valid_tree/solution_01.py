# DFS with iteration (stack)
def valid_tree(n, edges) -> bool:
    if len(edges) != n - 1:
        return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    parent = {0: -1}
    stack = [0]

    while stack:

        node = stack.pop()

        for neighbour in adj_list[node]:

            # Don't look at the trivial cycle
            if neighbour == parent[node]:
                continue

            # Check if we've already seen this node
            if neighbour in parent:
                # There must be a cycle
                return False

            # Otherwise, put this neighbour onto stack and record that it has been seen
            parent[neighbour] = node
            stack.append(neighbour)

    return len(parent) == n
