# 트리구성
# 이진탐색 (전위순회의 결과를 이용해 이진탐색으로 후위순회의 결과를 만들 수 있다)
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

preorder = []
root = 0


def postorder(start, end):
    if start > end:
        return

    root = preorder[start]
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1

    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)


# postorder(0, len(preorder) - 1)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, newNode):
        if self.root == None:
            self.root = newNode

        else:
            self.currNode = self.root
            while True:
                if newNode.data < self.currNode.data:
                    if self.currNode.left != None:
                        self.currNode = self.currNode.left
                    else:
                        self.currNode.left = newNode
                        break
                else:
                    if self.currNode.right != None:
                        self.currNode = self.currNode.right
                    else:
                        self.currNode.right = newNode
                        break

    def postOrder(self, root):
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


    def postOrder2(self, node):
        if node == None:
            return
        self.postOrder2(node.left)
        self.postOrder2(node.right)
        print(node.data)


tree = BinaryTree()
while True:
    try:
        value = int(input())
        # preorder.append(value)
        node = Node(value)
        tree.insert(node)
    except:
        break

tree.postOrder(tree.root)