# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 深度优先搜索 数组


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return
            root = TreeNode(postorder.pop())
            rootidx = dict_[root.val]
            root.right = helper(rootidx + 1, right)
            root.left = helper(left, rootidx - 1)
            return root
        dict_ = {rootval:idx for idx,rootval in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
