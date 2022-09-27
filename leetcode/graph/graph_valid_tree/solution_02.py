# DFS with recursion
def valid_tree(n, edges) -> bool:
    if len(edges) != n - 1:
        return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    seen = set()

    def dfs(node, parent):
        nonlocal seen

        if node in seen:
            return

        seen.add(node)
        for neighbour in adj_list[node]:

            if neighbour == parent:
                continue

            if neighbour in seen:
                return False

            result = dfs(neighbour, node)

            if not result:
                return False

        return True

    # We return true iff no cycles were detected, AND the entire graph has been reached.
    return dfs(0, -1) and len(seen) == n
