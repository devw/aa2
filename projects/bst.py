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
    # it returns None if the word is in the tree,
    # it returns the node containing the word
    node = get_root(tree)
    while node is not None and word != get_label(node):
        if word <= get_label(node):
            node = get_left(tree, node)
        else:
            node = get_right(tree, node)
    return node

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
