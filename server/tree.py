import json

# Since we're dealing with a tree structure, it's natural to use nested dictionaries.
# We create a subclass of dict
class TreeNode(dict):
    def __init__(self, name):
        self.__dict__ = self
        # to complete

    def add_child(self, child):
        # to complete
        pass

def build_product_tree():
    root = TreeNode("Animal")
    # to complete
  
    return root


treeData = build_product_tree()

tree = json.dumps([treeData])
