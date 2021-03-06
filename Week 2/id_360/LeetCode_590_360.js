/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

var postorder = function(root) {
    let res = []
    traversal(root, res);
    return res
};
function traversal(root, res) {
    if (root != null) {
        for (let i = 0; i < root.children.length; i++) {
            traversal(root.children[i], res)
        }
        res.push(root.val);
    }
}