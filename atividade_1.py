import random
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def draw_tree(root, filename="tree"):
    dot = Digraph(comment="Expression Tree")
    counter = [0] 

    def add_nodes_edges(node, parent=None):
        if node is None:
            return
        node_id = str(counter[0])
        counter[0] += 1

        dot.node(node_id, str(node.value)) 

        if parent is not None:
            dot.edge(parent, node_id)  

        add_nodes_edges(node.left, node_id)
        add_nodes_edges(node.right, node_id)

    add_nodes_edges(root)
    dot.render(filename, format="png", cleanup=True)
    print(f"Árvore gerada: {filename}.png")



def build_fixed_expression_tree():
 
    n7 = Node(7)
    n3 = Node(3)
    n5 = Node(5)
    n2 = Node(2)
    n10 = Node(10)
    n20 = Node(20)

 
    plus = Node("+")
    plus.left = n7
    plus.right = n3

    minus = Node("-")
    minus.left = n5
    minus.right = n2

    mult1 = Node("*")
    mult1.left = plus
    mult1.right = minus

    mult2 = Node("*")
    mult2.left = n10
    mult2.right = n20

    div = Node("/")
    div.left = mult1
    div.right = mult2

    return div


def build_random_expression_tree():
    operands = [str(random.randint(1, 20)) for _ in range(4)]
    operators = random.sample(["+", "-", "*", "/"], 3)


    n1, n2, n3, n4 = map(Node, operands)

    op1 = Node(operators[0])
    op1.left = n1
    op1.right = n2

    op2 = Node(operators[1])
    op2.left = n3
    op2.right = n4

    root = Node(operators[2])
    root.left = op1
    root.right = op2

    print("Expressão aleatória gerada:", 
          f"(({operands[0]} {operators[0]} {operands[1]}) {operators[2]} ({operands[2]} {operators[1]} {operands[3]}))")
    return root


if __name__ == "__main__":

    fixed_tree = build_fixed_expression_tree()
    draw_tree(fixed_tree, "arvore_fixa")


    random_tree = build_random_expression_tree()
    draw_tree(random_tree, "arvore_randomica")
