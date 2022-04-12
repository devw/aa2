import pytest
from projects.bst import get_words, get_tree


@pytest.mark.parametrize('url', [
    ("http://localhost:5501/projects/words.txt"),
])
def test_get_words(url):
    words = get_words(url)
    print(f"\n**words**: {words}")
    print(f"\nwords[0]: {words[0]}")
    print(f"\nwords[-1]: {words[-1]}")
    assert type(words) == type([])
    assert words[0] == "morose"
    assert words[-1] == "insécurité"


@pytest.mark.parametrize('list, expected', [
    ([], []),
    (['an'], [['an', None, None]]),
    (['an', 'ba'], [['an', None, 1], ['ba', None, None]]),
    (['ba', 'ab'], [['ba', 1, None], ['ab', None, None]]),
    (['ba', 'ab', 'ca'],  [['ba', 1, 2], ['ab', None, None], ['ca', None, None]]),
    (['ba', 'ab', 'ca', 'de'], [['ba', 1, 2], [
     'ab', None, None], ['ca', None, 3], ['de', None, None]])
])
def test_get_tree(list, expected):
    tree = get_tree(list)
    print(f"\ntest_get_tree: {tree} , {expected}")
    assert tree == expected
