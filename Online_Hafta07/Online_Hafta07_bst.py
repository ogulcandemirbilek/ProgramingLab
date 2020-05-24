class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key
def insert(root,node):
    if(root is None):
        root = node
    else:
        if(root.val<node.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right, node)
        else:
            if (root.left is None):
                root.left = node
            else:
                insert(root.left, node)
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val,end = " ")
        inorder(root.right)

def search(root,key):
    if(root is None or root.val==key):
        return root
    if(root.val<key):
        return search(root.right,key)
    return search(root.left,key)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif(key > root.val):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root

r=node(50)

insert(r,node(30))
insert(r,node(20))
insert(r,node(40))
insert(r,node(60))
insert(r,node(70))
insert(r,node(80))

inorder(r)

result = search(r,20)
print(result)

root = deleteNode(r, 20)
inorder(root)


insert(root, node(250))
inorder(root)
