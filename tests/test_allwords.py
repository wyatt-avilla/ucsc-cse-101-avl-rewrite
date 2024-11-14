from allwords import allwords
from allwords_more_range import range_queries

from avl import AVLTree


def test_allwords_basic(avl_tree: AVLTree) -> None:
    # Huge list of words
    inputs: list[str] = allwords

    # Test ranges and their expected counts
    range_test_cases: list[tuple[str, str, int]] = [
        ("a", "b", 25418),
        ("b", "c", 18414),
        ("c", "d", 32107),
        ("d", "e", 18734),
        ("e", "f", 14198),
        ("f", "g", 11894),
        ("g", "h", 10954),
        ("h", "i", 13744),
        ("i", "j", 13200),
        ("j", "k", 2841),
        ("k", "l", 3953),
        ("l", "m", 10003),
        ("m", "n", 19806),
        ("n", "o", 13459),
        ("o", "p", 12682),
        ("p", "q", 34861),
        ("q", "r", 1794),
        ("r", "s", 16784),
        ("s", "t", 38765),
        ("t", "u", 18820),
        ("u", "v", 22768),
        ("v", "w", 5330),
        ("w", "x", 6560),
        ("x", "y", 508),
        ("y", "z", 1144),
    ]

    # Insert all test values into the tree
    for value in inputs:
        avl_tree.insert(value)

    # Verify all range queries
    for start, end, expected_count in range_test_cases:
        actual_count = avl_tree.count_in_range(start, end)
        assert actual_count == expected_count, (
            f"Range query failed for range [{start}, {end}]: "
            f"expected {expected_count}, but got {actual_count}"
        )


def test_allwords_more_range(avl_tree: AVLTree) -> None:
    # Huge list of words
    inputs: list[str] = allwords

    # Test ranges and their expected counts
    range_test_cases = range_queries

    # Insert all test values into the tree
    for value in inputs:
        avl_tree.insert(value)

    # Verify all range queries
    for start, end, expected_count in range_test_cases:
        actual_count = avl_tree.count_in_range(start, end)
        assert actual_count == expected_count, (
            f"Range query failed for range [{start}, {end}]: "
            f"expected {expected_count}, but got {actual_count}"
        )
