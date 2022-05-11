# Write a function isBinarySearchTree
# which takes a tree as a parameter and returns a boolean
# to know if the tree put in parameter is binary search tree or not.
# How can we know if a binary

# What is an BST?
# An BST (ABR) is a binary tree which verifies these conditions
# - for each node of the tree the set of nodes of its left subtree are lower or equal
# - and the set of nodes of its right subtree are higher.

def isBinarySearchTree(tree):
    pass


tree = [('a', [1, 2]), ('b', [3, 4]), ('c', [-1, 5]),
        ('d', []), ('e', [-1, 6]), ('f', []), ('g', [])]

# print(isBinarySearchTree(tree) == False)


def hasLeftChild(node):
    # Write a function hasLeftChild which takes as parameters a node a return True if this node has a left child otherwise False
    if not node[1]:
        return False
    if node[1][0] == -1:
        return False
    return True


def hasRightChild(node):
    # Write a function hasLeftChild which takes as parameters a node a return True if this node has a left child otherwise False
    # aFilsDroit
    if not node[1]:
        return False
    if node[1][1] == -1:
        return False
    return True


tree = [('a', [1, 2]), ('b', [3, 4]), ('c', [-1, 5]),
        ('d', []), ('e', [-1, 6]), ('f', []), ('g', [])]


# Write the function parcoursInfixe which implements the Iterative Depth First Traversal and which takes as parameters: a tree, a indexSubTree and a procedure to visit a node.

tree = [(18, [1, 2]), (10, [3, 4]), (35, [5, -1]), (6, []), (14, []), (30, [])]


def isRightTreeEmpty(tree, indexNode):
    # sousArbreDroitEstVide
    # Write a function isRightTreeEmpty which takes as parameters a tree and a indexNode and it returns True if this tree has not a right node otherwise False
    node = tree[indexNode]
    if not hasRightChild(node):
        return True
    else:
        return False


def isLeftTreeEmpty(tree, indexNode):
    # sousArbreGaucheEstVide
    # Write a function isLeftTreeEmpty which takes as parameters a tree and a indexNode and it returns True if this tree has not a left node otherwise False
    node = tree[indexNode]
    if not hasLeftChild(node):
        return True
    else:
        return False


tree = [(18, [1, 2]), (10, [3, 4]), (35, [5, -1]), (6, []), (14, []), (30, [])]


# def get_root_index(tree):
#     if len(tree) == 0:
#         return None
#     index_child = []
#     for i in range(len(tree)):
#         index_child.extend(tree[i][1])
#     for j in range(len(tree)):
#         if j not in index_child:
#             return j


# def inOrderSearch(tree, index):
#     if not isLeftTreeEmpty(tree, index):
#         inOrderSearch(tree, tree[index][1][0])
#     print(tree[index][0])
#     if not isRightTreeEmpty(tree, index):
#         inOrderSearch(tree, tree[index][1][1])

def callback(node):     #
    print(node)

# Write the function inOrderSearch which implements the inorder search and which takes as parameters: a tree, a indexSubTree and a procedure to visit a node.
# isLeftTreeEmpty, isRightTreeEmpty


def inOrderSearch(tree, indexNode):
    if not isLeftTreeEmpty(tree, indexNode):
        inOrderSearch(tree, tree[indexNode][1][0])
    print(tree[indexNode])
    if not isRightTreeEmpty(tree, indexNode):
        inOrderSearch(tree, tree[indexNode][1][1])


def postOrderSearch(tree, index, callback):
    if not isLeftTreeEmpty(tree, index):
        postOrderSearch(tree, tree[index][1][0], callback)

    if not isRightTreeEmpty(tree, index):
        postOrderSearch(tree, tree[index][1][1], callback)
    callback(tree[index])


def preOrderSearch(tree, indexNode):
    print(tree[indexNode])
    if not isLeftTreeEmpty(tree, indexNode):
        preOrderSearch(tree, tree[indexNode][1][0])

    if not isRightTreeEmpty(tree, indexNode):
        preOrderSearch(tree, tree[indexNode][1][1])


# tree = [(3, [1, 2]), (1, []), (5, [])]
tree = [(18, [1, 2]), (10, [3, 4]), (35, [5, -1]), (6, []), (14, []), (30, [])]
tree = [('b', [1, 2]), ('a', []), ('c', [-1, 3]), ('d', [])]
tree = [('b', [1, 2]), ('a', []), ('c', [])]
print("\n\ninOrderSearch")
inOrderSearch(tree, 0)

# print("postOrderSearch")
# postOrderSearch(tree, 0, callback)

# print("preOrderSearch")
# preOrderSearch(tree, 0)

# get_root_index(tree)

# ParcoursInfixe(abr, get_indice_racine(abr), ma_fonction)
