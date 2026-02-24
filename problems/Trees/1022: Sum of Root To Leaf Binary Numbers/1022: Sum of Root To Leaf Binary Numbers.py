# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Solution, O(n) time, O(height) space
# Perform a depth first search, keeping track of the path from the root to the current node. 
# When we reach a leaf node, we add the path to the sum. 
# We can use bit manipulation to calculate the path value efficiently.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(node, pathSum):
            if not node:
                return 0
            
            pathSum = (pathSum << 1) | node.val
            
            if node.left is None and node.right is None:
                return pathSum
            
            return dfs(node.left, pathSum) + dfs(node.right, pathSum)
        
        return dfs(root, 0)


if __name__ == "__main__":
    solution = Solution()
    # root = [1,0,1,0,1,0,1]
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(solution.sumRootToLeaf(root)) 
