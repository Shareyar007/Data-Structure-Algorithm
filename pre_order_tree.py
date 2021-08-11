"""
            2
          /   \
        7       9
       / \       \
      1   6       8
         / \     / \
        5   10  3   4
"""
class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node

def create_tree():
    two = node(2)
    seven = node(7)
    nine = node(9)
    two.add_left(seven)
    two.add_right(nine)

    one = node(1)
    six = node(6)
    seven.add_left(one)
    seven.add_right(six)

    five = node(5)
    ten = node(10)
    six.add_left(five)
    six.add_right(ten)

    nine = node(9)
    two.add_right(nine)

    eight = node(8)
    nine.add_right(eight)

    three = node(3)
    four = node(4)
    eight.add_left(three)
    eight.add_right(four)
 
    return two

def pre_order(node):
    print(node.data, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


if __name__ == '__main__':
    tree = create_tree()
    print(tree.data)
    pre_order(tree)

