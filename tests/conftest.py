import pytest

from avl import AVLTree


@pytest.fixture
def avl_tree() -> AVLTree:
    return AVLTree()
