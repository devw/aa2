from projects.hash import get_hash
import pytest


@pytest.mark.parametrize('word', [
    ("dog"),
    ("cat")
])
def test_get_hash(word):
    hash = get_hash(word)
    print(f"get_hash = {word}, {hash}")
    assert type(hash) == int
    assert hash >= 0
    assert hash <= 255
