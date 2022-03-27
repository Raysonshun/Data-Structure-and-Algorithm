class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = f

res = []
queue = [a] # root

if a:
    while(queue):
        current_Node = queue.pop(0)
        res.append(current_Node.val)
        if current_Node.left:
            queue.append(current_Node.left)
        if current_Node.right:
            queue.append(current_Node.right)

print(res)
