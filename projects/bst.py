import ssl
from urllib.request import urlopen
import unittest

# res = ajouterfichier("/tmp/words.txt")
# print(res)
URL = "https://raw.githubusercontent.com/devw/spen/main/projects/words.txt"


def get_words(url=URL):
    response = urlopen(url, context=ssl._create_unverified_context())
    words = response.read().decode('utf-8').split("\n")
    return [word.lower() for word in words if word != '']


def get_label(node):
    if node:
        return node[0]
    return False


def get_root(tree):
    return tree[0]


def get_left(tree, node):
    if node[1] != None:
        return tree[node[1]]
    return None


def get_right(tree, node):
    if node[2] != None:
        return tree[node[2]]
    return None


def get_tree(words):
    # For a given list of words, it returns the tree as a list.
    # Each element of the list is a list (node) having three parameters (data, left_index, right_index)
    tree = []

    if words == []:
        return tree

    tree.append([words.pop(0), None, None])

    for word in words:
        node_index = 0
        while node_index != None:
            last_node_index = node_index
            if word > tree[node_index][0]:
                node_index = tree[node_index][2]
                side = "right"
            else:
                node_index = tree[node_index][1]
                side = "left"

        if side == "right":
            tree[last_node_index][2] = len(tree)
        else:
            tree[last_node_index][1] = len(tree)

        tree.append([word, None, None])

    return (tree)


def search_bst(tree, word):
    node = tree[0]

    while node[0] != word and node != None:
        if word < node[0]:
            if node[1] == None:
                return None
            else:
                node = tree[node[1]]
        else:
            if node[2] == None:
                return None
            else:
                node = tree[node[2]]
    return node


def search_bst_2(tree, word):
    subtree = tree

    while subtree[0] != word and subtree[0] != []:
        if word < subtree[0]:
            if subtree[1] == []:
                return []
            else:
                subtree = subtree[1]
        else:
            if subtree[2] == []:
                return []
            else:
                subtree = subtree[2]
    return subtree[0]


tree_2 = ['b', ['a', [], ['ab', [], []]], ['d', [], []]]
res = search_bst_2(tree_2, 'ab')
print("search_bst_2:", res)
### Testing ###


class TestGraphicalInterface(unittest.TestCase):

    def test_get_words(self):
        URL = "https://raw.githubusercontent.com/devw/spen/main/projects/words.txt"
        words = get_words(URL)
        self.assertTrue(words[0] == 'escape')
        self.assertTrue(words[-1] == 'find')

    def test_get_tree(self):
        # test scenario 1
        input = []
        output = []
        self.assertTrue(get_tree(input) == output)

        # test scenario 2
        input = ['a']
        self.assertTrue(get_tree(input) == [['a', None, None]])

        # test scenario 2
        inp = ['a', 'b']
        out = [['a', None, 1], ['b', None, None]]
        self.assertTrue(get_tree(inp) == out)

        # test scenario 3
        inp = ['b', 'a']
        out = [['b', 1, None], ['a', None, None]]
        self.assertTrue(get_tree(inp) == out)

        # test scenario 4
        inp = ['b', 'a', 'ab', 'd']
        out = [['b', 1, 3], ['a', None, 2], [
            'ab', None, None], ['d', None, None]]
        self.assertTrue(get_tree(inp) == out)

    def test_search_bst(self):
        tree = get_tree(['b', 'a', 'ab', 'd'])
        # test scenario 1
        self.assertIsNone(search_bst(tree, 'f'))

        # test scenario 2
        self.assertTrue(search_bst(tree, 'a') == ['a', None, 2])

        # test scenario 3
        self.assertTrue(search_bst(tree, 'b') == ['b', 1, 3])


if __name__ == '__main__':
    unittest.main()
#print(get_tree(['B', 'C', 'A']))
