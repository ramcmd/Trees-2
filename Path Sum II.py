# TC: O(2n)
# SC: O(1) 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from copy import deepcopy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        arr = []
        self.TargetSum = targetSum
        currsum = 0
        self.traversal(root, currsum, arr)
        return self.res
    
    def traversal(self, root, currsum, arr):
        
        if root == None:
            return
            
        arr.append(root.val)
        
        currsum += root.val
        
        self.traversal(root.left, currsum, arr)
        
        if root.left == None and root.right == None:
            if currsum == self.TargetSum:
                temp = deepcopy(arr)
                self.res.append(temp)
        
        self.traversal(root.right, currsum, arr)
        arr.pop()
        
    
        
        
        