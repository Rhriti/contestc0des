# import networkx as nx
# import numpy as np

# def maximize_absolute_sum(a, b):
#     n = len(a)
#     m = len(b)

#     # Create bipartite graph
#     G = nx.Graph()
#     G.add_nodes_from(range(n), bipartite=0)
#     G.add_nodes_from(range(n, n + m), bipartite=1)

#     # Add edges with weights equal to absolute differences
#     for i in range(n):
#         for j in range(m):
#             weight = abs(a[i] - b[j])
#             G.add_edge(i, j + n, weight=weight)

#     # Find maximum-weight matching using Kuhn-Munkres algorithm
#     matching = nx.bipartite.maximum_matching(G)

#     # Calculate the maximum absolute sum
#     max_absolute_sum = sum(abs(a[i] - b[matching[i]]) for i in range(n))

#     return max_absolute_sum

# # Example usage:
# a = [5,6,2]
# b = [1,2,7,7,9]
# result = maximize_absolute_sum(a, b)
# print("Maximum absolute sum:", result)


def maximize_absolute_sum(a, b):
    n = len(a)
    m = len(b)

    # Initialize cost matrix
    cost_matrix = [[abs(a[i] - b[j]) for j in range(m)] for i in range(n)]

    # Step 1: Subtract the smallest value in each row from all the values in that row
    for i in range(n):
        min_value = min(cost_matrix[i])
        for j in range(m):
            cost_matrix[i][j] -= min_value

    # Step 2: Subtract the smallest value in each column from all the values in that column
    for j in range(m):
        min_value = min(cost_matrix[i][j] for i in range(n))
        for i in range(n):
            cost_matrix[i][j] -= min_value

    # Step 3: Cover all zeros using minimum number of lines
    row_covered = [False] * n
    col_covered = [False] * m
    marked_zeros = []

    for i in range(n):
        for j in range(m):
            if cost_matrix[i][j] == 0 and not row_covered[i] and not col_covered[j]:
                marked_zeros.append((i, j))
                row_covered[i] = True
                col_covered[j] = True
                break

    # Repeated steps until all zeros are covered
    while len(marked_zeros) < n:
        # Find an uncovered zero in the cost matrix
        i, j = -1, -1
        for i in range(n):
            if not row_covered[i]:
                for j in range(m):
                    if not col_covered[j] and cost_matrix[i][j] == 0:
                        break

        # If no uncovered zero is found, go to step 5
        if i == n or j == m:
            break

        # Mark the found zero
        marked_zeros.append((i, j))
        row_covered[i] = True
        col_covered[j] = True

        # Find a non-covered zero in the row
        for jj in range(m):
            if cost_matrix[i][jj] == 0 and not col_covered[jj]:
                marked_zeros.append((i, jj))
                row_covered[i] = True
                col_covered[jj] = True
                break

        # If no non-covered zero is found, go to step 5
        if jj == m:
            break

    # Step 4: Determine the smallest uncovered value and add it to all covered values
    min_uncovered_value = min(cost_matrix[i][j] for i in range(n) for j in range(m) if not row_covered[i] and not col_covered[j])
    for i in range(n):
        for j in range(m):
            if row_covered[i] and col_covered[j]:
                cost_matrix[i][j] += min_uncovered_value
            elif not row_covered[i] and not col_covered[j]:
                cost_matrix[i][j] -= min_uncovered_value

    # Repeat steps 2-4 until all zeros are covered
    while len(marked_zeros) < n:
        # Repeat steps 2-4

        # Step 2
        for i in range(n):
            min_value = min(cost_matrix[i])
            for j in range(m):
                cost_matrix[i][j] -= min_value

        # Step 3
        row_covered = [False] * n
        col_covered = [False] * m

        for i in range(n):
            for j in range(m):
                if cost_matrix[i][j] == 0 and not row_covered[i] and not col_covered[j]:
                    marked_zeros.append((i, j))
                    row_covered[i] = True
                    col_covered[j] = True
                    break

        # Step 4
        min_uncovered_value = min(cost_matrix[i][j] for i in range(n) for j in range(m) if not row_covered[i] and not col_covered[j])
        for i in range(n):
            for j in range(m):
                if row_covered[i] and col_covered[j]:
                    cost_matrix[i][j] += min_uncovered_value
                elif not row_covered[i] and not col_covered[j]:
                    cost_matrix[i][j] -= min_uncovered_value

    # Extract the maximum-weight matching
    matching = {}
    for i, j in marked_zeros:
        matching[i] = j

    # Calculate the maximum absolute sum
    max_absolute_sum = sum(abs(a[i] - b[matching[i]]) for i in range(n))

    return max_absolute_sum, matching

# Example usage:
a = [6,5,2]
b = [1,2,7,7,9]
result, matching = maximize_absolute_sum(a, b)
print("Maximum absolute sum:", result)
print("Matching indices:", matching)
