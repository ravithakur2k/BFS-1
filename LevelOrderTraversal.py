from typing import List, Optional
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The intuition here is to use a queue and then pop the value from the queue and then add its
# neighbors which will give a level order traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            subResult = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    subResult.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(subResult)

        return result


# Done using recursion where we pass the level as a parameter and then if at any instance if the length of result array is equal to level then we add an empty list.
# If its not then we get the sub list and append the root value

    def levelOrderRecursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.helper(root, 0)
        return self.result

    def helper(self, root, level):
        if not root:
            return None

        if len(self.result) == level:
            self.result.append([])

        self.result[level].append(root.val)

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
