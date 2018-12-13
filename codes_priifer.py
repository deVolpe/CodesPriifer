from collections import Counter


def get_new_tree(node, tree, length):
    for i in range(length):
        if (node, i) in tree:
            tree.remove((node, i))
            break
        elif (i, node) in tree:
            tree.remove((i, node))
            break

    return tree, i


def counting_edges_of_each_node(arr):
    count = Counter(arr)
    return count


def intermediate_array(tree):
    inter = sum([list(item) for item in tree], [])
    return inter


def nodes_with_one_edge(count):
    nodes = list(filter(lambda x: count[x] < 2, count))
    return nodes


def codes_priifer(tree):
    res = list()
    length = len(tree)
    i = 0
    while i < length - 1:
        inter = intermediate_array(tree)
        count = counting_the_tree_of_each_node(inter)
        nodes = nodes_with_one_edge(count)
        tree, neigh = get_new_tree(min(sorted(nodes)), tree, length)
        res.append(neigh)
        i += 1
    print(res)


if __name__ == '__main__':
    codes_priifer(tree={(0, 1), (0, 2), (1, 3), (1, 4), (2, 5),
                       (2, 6), (4, 7), (7, 8), (7, 9)}
                 )
