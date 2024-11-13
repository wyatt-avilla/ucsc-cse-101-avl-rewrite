from avl import AVLTree


def test_simple_input(avl_tree: AVLTree) -> None:
    # Values inserted into the AVL tree
    inputs = [
        "10", "20", "30", "40", "50",
        "60", "70", "80", "90", "99",
        "15", "14", "12", "25", "28",
        "95", "35", "38", "11", "23",
        "22",
    ]

    # Test ranges and their expected counts
    range_test_cases: list[tuple[str, str, int]] = [
        ("10", "20", 6),   # Testing small range at start
        ("10", "99", 21),  # Testing full range
        ("45", "87", 4),   # Testing middle range
        ("21", "39", 7),   # Testing range with multiple elements
        ("21", "79", 11),  # Testing larger middle range
        ("29", "79", 7),   # Testing range with specific bounds
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
