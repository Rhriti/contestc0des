class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
    def update(self, v, tl, tr, l, r):
        if l > r:
            return
        
        if l == tl and r == tr:
            self.tree[v] += 1
            self.lazy[v] += 1
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm))
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
            self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1]) + self.lazy[v]
    
    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        
        if l == tl and r == tr:
            return self.tree[v]
        
        tm = (tl + tr) // 2
        return max(self.query(2 * v, tl, tm, l, min(r, tm)),
                   self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)) + self.lazy[v]

    def checkOverlap(self, l, r):
        # Replace 'treeSize' with the size of your tree
        treeSize = len(self.tree) // 4  # Adjust this based on your segment tree size
        val = self.query(1, 0, treeSize - 1, l, r)
        
        if val == 0:
            return "No Overlap"
        elif val == r - l + 1:
            return "Complete Overlap"
        else:
            return "Partial Overlap"


# Usage Example:
n = 10  # Adjust this based on your requirements
segTree = SegmentTree(n)
segTree.update(1, 0, n - 1, 1,2)  # Example: Inserting range [2, 5]
print(segTree.query())
segTree.update(1,0,4,5)