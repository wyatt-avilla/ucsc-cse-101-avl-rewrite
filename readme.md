# HW AVL: Life is all about balance

© C. Seshadhri, 2020

- All code must be written in C/C++.
- Be careful about using built-in libraries or data structures. The assignment
  instructions will specify what is acceptable and what is not. If you have any
  doubts, please ask the instructors or TAs.

---

## Problem Description

To get half credit is really easy. To get full credit is hard. You have been
forewarned. But you will learn a lot trying to get full credit.

Read this document carefully. Half the questions on Piazza can be answered by
just reading the instructions. Also, the algorithm for this assignment requires
a fair bit of thought, so read the suggestions carefully.

**Main objective:** Design a fast data structure to perform insertions and range
queries on text. The input file will have a long list of words to insert,
interspersed with range queries that determine the number of words seen so far
within a given range. For example, if the range is “ab” to “bc”, find the number
of words lexicographically between “ab” and “bc”.

This assignment is challenging because the data structure needs to handle up to
a million inserts and two million range queries, requiring high efficiency.

You **cannot** use built-in data structures for storing words or answering range
queries. You can use libraries for I/O and string processing.

**Setup:** Use the Codio unit for this assignment. There is a directory
“Wordrange” with test input/output files, which are explained later. All code
must be written in this directory, not in any subdirectory. Check the README for
more details.

---

## Format and Output

- Provide a Makefile. Running `make` should create an executable `wordrange`.
- Run the executable with two command line arguments: the input file and the
  output file.
- Provide a README with usage explanations and a description of involved files.
- Cite any sources used, including online code, past course code, or extensive
  discussions with someone.

The input file lines will be of the following two forms:

- `i <STRING>` - Insert the string into your data structure. If it’s already
  present, do not insert again. Each word should appear only once.
- `r <STRING1> <STRING2>` - Count the number of strings in the data structure
  that are lexicographically between `STRING1` and `STRING2`.

**Note:** The output should be written in the output file, with each range size
printed on a separate line.

---

## Data Structure Instructions

You cannot use built-in data structures in C++. A standard BST is enough for
half credit, while an AVL tree is required for full credit.

For full credit, handle a million range queries efficiently by storing subtree
sizes at every node, allowing a Θ(log n) algorithm for answering range queries.

Hints:

- **Recursive Approach**: To find the range size in the subtree rooted at node
  `x`, compare the key at `x` with `str1` and `str2`, leading to three possible
  scenarios, which can be resolved by recursive calls.
- Store subtree sizes to reduce recursive calls, enabling "less than" or
  "greater than" queries to be answered with at most one recursive call.

---

## Tips for Implementation

1. **Start with the half-credit solution** and ensure it works.
2. **AVL Insertion**: Understand AVL insertion well. Use resources like the
   Wikipedia article on [AVL trees](https://en.wikipedia.org/wiki/AVL_tree).
3. **Node Properties**: Store heights for the AVL property and subtree sizes for
   range queries.
4. **Rotations**: Code up left and right rotations as separate functions,
   carefully updating heights and subtree sizes.
5. **Edge Cases**: Handle cases where rotations affect null children and the
   root.
6. **Recursion and Parent Pointers**: Ensure parents are updated whenever
   children change.

## Test Cases

1. **simple-input.txt, simple-output.txt**: Inserts a few numbers to check basic
   functionality.
2. **allwords-basic.txt, allwords-basic-output.txt**: Inserts all English words
   and computes a few range queries.
3. **allwords-more-range.txt, allwords-more-range-output.txt**: 1.8 million
   operations to test efficiency.

---

## Grading

1. **(10 points)**: Complete solution with three million operations in under a
   minute.
2. **(7 points)**: Handle about a million operations in a minute.
3. **(5 points)**: Pass small test cases using a standard BST with range
   searching across the entire tree.

---

## Comments

Self-balancing trees are highly efficient, enabling fast range queries. BSTs are
adaptable, allowing range searches to become quick with stored subtree sizes.

For further BST practice, try
[these problems on Medium](https://medium.com/@codingfreak/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f).
