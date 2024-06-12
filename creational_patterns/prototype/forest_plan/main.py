"""
Client code that shows realizing prototype patterns.
"""
from creational_patterns.prototype.forest_plan\
    .trees import Tree


if __name__ == "__main__":
    trees = []
    count_trees = 20
    tree_names = ["Oak", "Maple", "Spruce"]

    coord_x = 0
    coord_y = 0

    limit = 100

    tree_donor = Tree()
    for tree_name in tree_names:
        tree_clone = tree_donor.clone()
        tree_clone.name = tree_name

        # for number in range(count_trees):
        #     tree_clone_coord = tree_clone.clone()
        #     tree_clone_coord.coord_x = coord_x
        #     tree_clone_coord.coord_y = coord_y
        #     trees.append(tree_clone_coord)
        #
        #     coord_y += 5
        # coord_x += 5

    # for tree in trees:
    #     print(tree)
