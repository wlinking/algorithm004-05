# 给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list:
        rdata = []
        if root:
            rdata.append(root.val)

            for c in root.children:
                rdata.extend(self.preorder(c))

        return rdata


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = Node(1, [])
    r3 = Node(3, [])
    r2 = Node(2, [])
    r4 = Node(4, [])
    r5 = Node(5, [])
    r6 = Node(6, [])

    root.children = [r3, r2, r4]
    r3.children = [r5, r6]

    s = Solution()
    print(s.preorder(root))
