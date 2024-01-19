class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)  # Initializing the segment tree with zeros
        self.lazy = [0] * (4 * n)  # Initializing the lazy tree with zeros
        self.n = n

    # Utility function to update the segment tree
    def update(self, index, left, right, ql, qr, value):
        # Apply pending updates if any
        if self.lazy[index]:
            self.tree[index] += self.lazy[index]
            if left != right:
                self.lazy[2 * index + 1] += self.lazy[index]
                self.lazy[2 * index + 2] += self.lazy[index]
            self.lazy[index] = 0

        # No overlap
        if qr < left or ql > right:
            return

        # Total overlap
        if ql <= left and qr >= right:
            self.tree[index] += value
            if left != right:
                self.lazy[2 * index + 1] += value
                self.lazy[2 * index + 2] += value
            return

        mid = (left + right) // 2
        self.update(2 * index + 1, left, mid, ql, qr, value)
        self.update(2 * index + 2, mid + 1, right, ql, qr, value)

    # Function to query the segment tree
    def query(self, index, left, right, ql, qr):
        if self.lazy[index]:
            self.tree[index] += self.lazy[index]
            if left != right:
                self.lazy[2 * index + 1] += self.lazy[index]
                self.lazy[2 * index + 2] += self.lazy[index]
            self.lazy[index] = 0

        if ql <= left and qr >= right:
            return self.tree[index]

        if qr < left or ql > right:
            return 0

        mid = (left + right) // 2
        return self.query(2 * index + 1, left, mid, ql, qr) + self.query(2 * index + 2, mid + 1, right, ql, qr)


# Example usage:
N = 10  # Number of elements or range size
seg_tree = SegmentTree(N)

# Update the segment tree with a range [2, 5] with value 1
seg_tree.update(0, 0, N - 1, 2, 5, 1)

# Query the segment tree to check overlap with range [3, 6]
result = seg_tree.query(0, 0, N - 1, 3, 6)
print("Overlap value for the range [3, 6]:", result)
