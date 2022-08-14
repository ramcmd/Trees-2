# TC: O(2n) where n i the no of nodes
# SC: O(1) no auxillary data structure used
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        self.traversal(root, 0)
        
        return self.result
        
        
    
    def traversal(self, root, currsum):
        
        if root == None:
            return
        
        currsum = currsum*10 + root.val
        
        self.traversal(root.left, currsum)
        
        if root.left == None and root.right == None:
            self.result += currsum
            
        self.traversal(root.right, currsum)
        

        
        
        
        