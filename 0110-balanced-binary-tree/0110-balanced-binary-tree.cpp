/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int checkHeight(TreeNode* root){
        if(root == nullptr) return 0; 

        int rightresult = checkHeight(root->right); 
        if(rightresult == -1) return -1; 
        int leftresult = checkHeight(root->left); 
        if(leftresult == -1) return -1; 

        if(abs(leftresult - rightresult) > 1) return -1; 

        return 1 + max(leftresult, rightresult); 
    }
    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1; 
        
    }
};