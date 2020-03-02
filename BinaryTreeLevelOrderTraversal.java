public class BinaryTreeLevelOrderTraversal {
    /**
     * @param root: A Tree
     * @return: Level order a list of lists of integer
     */
    public List<List<Integer>> levelOrder(TreeNode root) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        List<TreeNode> nodes = new ArrayList<TreeNode>();
        nodes.add(root);
        while(nodes.size() != 0){
            List<TreeNode> newNodes = new ArrayList<TreeNode>();
            List<Integer> values = new ArrayList<Integer>();
            for(TreeNode node: nodes){
                values.add(node.val);
                if(node.left != null) newNodes.add(node.left);
                if(node.right != null) newNodes.add(node.right);
            }
            results.add(values);
            nodes = newNodes;
        }
        return results;
    }
}