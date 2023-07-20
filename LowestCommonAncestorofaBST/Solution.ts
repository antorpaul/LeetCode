/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null | undefined {
    if(p === null || q === null || root === null)
    {
        return;
    }

    if(root.left === null || root.right === null)
    {
        return;
    }

	// if there is ever a split between which branch p or q is located, that's the LCA
    if(p.val > root.val && q.val > root.val)
    {
        lowestCommonAncestor(root.right, p, q);
    }

    if(p.val < root.val && q.val < root.val)
    {
        lowestCommonAncestor(root.left, p, q);
    }

    if(root.val === p.val || root.val === q.val)
    {
        return root.val === p.val ? p : q;
    } else {
        return root;
    }
};