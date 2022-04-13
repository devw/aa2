from projects.hash import get_hash
import pytest


@pytest.mark.parametrize('words', [
    (["dog"]),
    (["cat"]),
    (["cr", "rc"])
])
def test_get_hash(words):
    word = words[0]
    hash = get_hash(word)
    print(f"get_hash = {word}, {hash}")
    assert type(hash) == int
    assert hash >= 0
    assert hash <= 255
    if len(words) > 1:
        hash_1 = get_hash(word[0])
        hash_2 = get_hash(word[1])
        print(f"hash_1 vs hash_2 = {hash_1}, {hash_2}")
        assert hash_1 is not hash_2
