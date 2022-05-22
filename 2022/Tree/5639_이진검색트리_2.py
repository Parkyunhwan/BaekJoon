import sys
sys.setrecursionlimit(10**6)
root = None
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(newNode):
    global root
    if root == None:
        root = newNode

    else:
        currNode = root
        while True:
            if newNode.data < currNode.data:
                if currNode.left != None:
                    currNode = currNode.left
                else:
                    currNode.left = newNode
                    break
            else:
                if currNode.right != None:
                    currNode = currNode.right
                else:
                    currNode.right = newNode
                    break


def postOrder(root):
    result, stack = [], []
    stack.append(root)

    while stack:
        curr = stack.pop()
        result.append(curr)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    while result:
        print(result.pop().data)

while True:
    try:
        node = Node(int(input()))
        insert(node)
    except:
        break

postOrder(root)