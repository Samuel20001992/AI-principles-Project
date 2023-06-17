class Node:
    def __init__(self, name, quality, level, children=None) -> None:
        self.name = name
        self.quality = quality
        self.level = level
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

def get_child_with_max_value(parent):
    max_child = None
    max_value = float('-inf')
    
    for child in parent.children:
        if child.quality > max_value:
            max_child = child
            max_value = child.quality
    
    return max_child

def get_child_with_min_value(parent):
    min_child = None
    min_value = float('+inf')
    
    for child in parent.children:
        if child.quality < min_value:
            min_child = child
            min_value = child.quality
    
    return min_child

def print_tree(node, level=0):
    # Print the current node
    indent = "      " * level
    print(indent  + ' '+ str(node.name) + ' quality ' + str(node.quality))

    # Print children recursively
    for child in node.children:
        print_tree(child , level + 1)


root = Node("Addis Ababa", 0, 1)

child1 = Node("Ambo", 0, 2)
child2 = Node("Buta Jirra", 0, 2)
child3 =  Node("Adama", 0, 2)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)


grandchild1 =  Node("Gedo", 0, 3)
grandchild2 = Node("Nekemte", 0, 3)
child1.add_child(grandchild1)
child1.add_child(grandchild2)


grandchild3 =  Node("Worabe", 0, 3)
grandchild4 =  Node("Wolkite", 0, 3)
child2.add_child(grandchild3)
child2.add_child(grandchild4)

grandchild5 =  Node("Mojo", 0, 3)
grandchild6 =  Node("Diredawa", 0, 3)
child3.add_child(grandchild5)
child3.add_child(grandchild6)

greatgrandchild1 =  Node("Fincha",5,4)
greatgrandchild2 =  Node("Shambu",4,4)
grandchild1.add_child(greatgrandchild1)
grandchild1.add_child(greatgrandchild2)

greatgrandchild3 =  Node("Gimbi",8,4)
greatgrandchild4 =  Node("Limu",8,4)
grandchild2.add_child(greatgrandchild3)
grandchild2.add_child(greatgrandchild4)


greatgrandchild5 =  Node("Hossana",6,4)
greatgrandchild6 =  Node("Durame",5,4)
grandchild3.add_child(greatgrandchild5)
grandchild3.add_child(greatgrandchild6)


greatgrandchild7 =  Node("Bench Naji",5,4)
greatgrandchild8 =  Node("Tepi",6,4)
grandchild4.add_child(greatgrandchild7)
grandchild4.add_child(greatgrandchild8)


greatgrandchild9 =  Node("Kaffa",7, 4)
greatgrandchild10 =  Node("Dilla",9, 4)
grandchild5.add_child(greatgrandchild9)
grandchild5.add_child(greatgrandchild10)


greatgrandchild11 =  Node("Chiro",6, 4)
greatgrandchild12 =  Node("Harar",10, 4)
grandchild6.add_child(greatgrandchild11)
grandchild6.add_child(greatgrandchild12)


minmax_1 = [grandchild1, grandchild2, grandchild3, grandchild4, grandchild5, grandchild6]
minmax_2 = [child1, child2, child3]
minmax_3 = [root]

level_2 = []
for parent in minmax_1:
    parent = get_child_with_max_value(parent)
    level_2.append(parent)


grandchild1.quality = level_2[0].quality
grandchild2.quality = level_2[1].quality
grandchild3.quality = level_2[2].quality
grandchild4.quality = level_2[3].quality
grandchild5.quality = level_2[4].quality
grandchild6.quality = level_2[5].quality

level_1 = []
for parent in minmax_2:
    parent = get_child_with_min_value(parent)
    level_1.append(parent)


child1.quality = level_1[0].quality
child2.quality = level_1[1].quality
child3.quality = level_1[2].quality



parent = get_child_with_max_value(root)
level_0 = []
level_0.append(parent)

root.quality = level_0[0].quality

print_tree(root)




