def morris(root):
    result = []
    while root:
        if not root.left:
            result.append(root.val)
            root = root.right
        else:
            predecessor = root.left
            while predecessor.right and predecessor.right != root:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = root
                root = root.left
            # predecessor.right == current, meaning we're going back to the root
            else:
                predecessor.right = None
                result.append(root.val)
                root = root.right
                
    return result