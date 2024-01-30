import sys
sys.path.append('F:\GitHubCode\CS61A\Week06\lab05')
from lab05 import tree, is_leaf, label, print_tree, branches
#TODO Solution Of Questions 1.1
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(x) for x in t[1:]])
    
#TODO Solution Of Question 1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    
    >>> t = tree(1, [tree(5, [tree(1),tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(tree) for tree in t[1:]])
    
#TODO Solution Of Question 1.3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                         [tree(3),
    ...                          tree(4)]),
    ...                  tree(5,
    ...                       [tree(6,
    ...                             [tree(7)]),
    ...                        tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(pow(label(t), 2))
    else:
        branches = [square_tree(tree) for tree in t[1:]]
        return tree(pow(label(t), 2), branches)
    
#TODO Solution Of Question 1.4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7,[tree(3),tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """
    if not tree:
        return None

    if label(tree) == x:
        return [label(tree)]

    for subtree in branches(tree):
        path = find_path(subtree, x)
        if path:
            return [label(tree)] + path

    return None

#TODO Solution Of Question 1.4
def prune_binary(t, nums):
    """Write a function that takes in a tree consisting of ’0’s and ’1’s t and a list of ”binary
    numbers” nums and returns a new tree that contains only the numbers in nums that
    exist in t. If there are no numbers in nums that exist in t, return None.

    >>> t = tree('1',[tree('0',[tree('0'),tree('1')]), tree('1',[tree('0')])])
    >>> str_list = ['01', '110', '100']
    >>> print(prune_binary(t, str_list))
    ['1', ['0', ['0']], ['1', ['0']]]
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [x[1:] for x in nums if x[0] == label(t)]
        new_branches = []
        for branch in branches(t):
            pruned_branch = prune_binary(branch, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)