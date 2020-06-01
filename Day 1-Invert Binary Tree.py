# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def swapNodes(node):
    if node==None:
        return
    else:
        temp = node
        swapNodes(node.left)
        swapNodes(node.right)
        
        temp = node.left
        node.left = node.right
        node.right = temp
    
        
    return node
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return swapNodes(root)
       
