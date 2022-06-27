# Exe A
"""
Let's suppose to implement a tree data structure via a list where the second item represents the pointers to the children nodes (line 329). 

Select the options that allows displaying the size of the tree.  

"""

tree = [["R", (1, 2, 3)], ["A", (4, 5)], ["B", ()],
        ["C", ()], ["D", ()], ["E", ()]]

print(len(tree))

# Exe B

"""
Let's suppose to implement a tree data structure via a list where the second item represents a subtree (line 193). 
Select the option that allows reading the data at level 2.  
tree = ["R", [ ["A", [ ["D", [] ], ["E", [] ]] ], ["B",[] ], ["C", []] ] ]
"""

tree = ["R", [["A", [["D", []], ["E", []]]], ["B", []], ["C", []]]]


# Exe 3
"""
Let's suppose to implement a tree data structure via a list where the second item represents the pointers to the children nodes (line 329).  Select the options that allow displaying the leaves nodes. 

 

"""

tree = [["R", (1, 2, 3)], ["A", (4, 5)], ["B", ()],
        ["C", ()], ["D", ()], ["E", ()]]

# Exercise 1


"""
Let's suppose to implement a tree data structure via a list where the second item represents a subtree (line 9). Select the option that allows access to the nodes' data at level 2.   

Hint [1,2] + [3] = [1, 2, 3]
"""


#         R
#       / | \
#     A   B  C
#    / \    /
#   D   E  F
#         /
#        G

tree = ["R", [["A", [["D", []], ["E", []]]],
              ["B", []], ["C", [["F", [["G", []]]]]]]]

print(tree[1][2][1][0][1][0])


[x[0] for x in tree[1]]


# exercise 2

"""
Let's suppose to implement a tree data structure via a list where the second item represents the pointers to the children nodes (line 53).   
What is the output of the "foo" function (line 55).   

Hint: the max() function returns the largest item in an array.
"""

#         1
#       / | \
#     3   2  4
#    / \    /
#   6   5  7


def foo(tree):
    arr = []
    for x in tree:
        num = len(x[1]) + 1
        arr.append(num - int(x[0]))
    return max(arr)


tree = [["1", [1, 2, 3]], ["3", [4, 5]], ["2", []],
        ["4", [6]], ["6", []], ["5", []], ["7", []]]

print(foo(tree))


# Exercise 3
"""
Let's suppose to implement a tree data structure via a list where the second item represents the pointers to the children nodes (line 65).   What is the output of the "bar" function (line 76).  

Hint: the max() function returns the largest item in an array.
"""

#         R
#       / | \
#     A   B  C
#    / \
#   D   E

tree = ["R", [["A", [["D", []], ["E", []]]], ["B", []], ["C", []]]]


def bar(tree):
    arr = []
    if not len(tree) == 0 and len(tree[1]) == 0:
        return 0
    else:
        for subtree in tree[1]:
            arr.append(bar(subtree))
        return 1 + max(arr)


print(bar(tree))
