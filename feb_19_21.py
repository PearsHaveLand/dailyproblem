# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# Symbol defining a non-value in the serialized tree
VALUE_NONE = 'None'
OPEN_LEFT = '<left>'
CLOSE_LEFT = '</left>'
OPEN_RIGHT = '<right>'
CLOSE_RIGHT = '</right>'
OPEN_ROOT = '<root>'
CLOSE_ROOT = '</root>'
NEWLINE = '\n'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root, is_root=True, height=0):
    str_tree = ""
    spaces = "  "

    # If root has a value
    if root != None:
        
        if is_root:
            str_tree += OPEN_ROOT + NEWLINE

        # Add spaces for prettier output
        for i in range(height):
            spaces += "  "

        if root.val == None:
            str_tree += spaces + VALUE_NONE + NEWLINE
        else:
            # We concatenate the root to the current tree
            str_tree += spaces + '\'' + root.val + '\'' + NEWLINE

        # Add left child to serialization
        if root.left != None:
            str_tree = str_tree + spaces + OPEN_LEFT + NEWLINE + serialize(root.left, False, height+1) + spaces + CLOSE_LEFT + NEWLINE    
        #else: 
        #    str_tree = str_tree + spaces + OPEN_LEFT + NEWLINE + spaces + CLOSE_LEFT + NEWLINE    

        # Add right child to serialization
        if root.right != None:
            str_tree = str_tree + spaces + OPEN_RIGHT + NEWLINE + serialize(root.right, False, height+1) + spaces + CLOSE_RIGHT + NEWLINE
        #else:
        #    str_tree = str_tree + spaces + OPEN_RIGHT + NEWLINE + spaces + CLOSE_RIGHT + NEWLINE

        if is_root:
            str_tree += CLOSE_ROOT

    return str_tree

# Recursively parses formatted tree list and constructs tree
def deserialize_list(tree_list):
    tree = None
    #while len(tree_list) > 0:

    curr_node = tree_list[0]

    # Handle actual values first, since they don't necessarily require a recursive call
    if curr_node[0] == '\'':

        # Remove quotes and set value
        tree = Node(curr_node.replace('\'', ''))

        # Handle the rest of the list
        tree_list = tree_list[1::]

        # print("value '", tree.val, "' found; list remainder:\n", tree_list)

        curr_node = tree_list[0]

    # When opening to a new node, remove node delimiter and deserialize the rest of the list
    if curr_node == OPEN_LEFT:

        tree_list = tree_list[1::]
        # print("left child found, list remainder:\n", tree_list)

        tree.left, tree_list = deserialize_list(tree_list)
        curr_node = tree_list[0]
        # print(curr_node)    

    # When opening to a new node, remove node delimiter and deserialize the rest of the list
    if curr_node == OPEN_RIGHT:

        tree_list = tree_list[1::]

        # print("right child found, list remainder:\n", tree_list)

        tree.right, tree_list = deserialize_list(tree_list)
        curr_node = tree_list[0]    

    # When opening to a new node, remove node delimiter and deserialize the rest of the list
    elif curr_node == OPEN_ROOT:
        tree_list = tree_list[1::]
        tree, tree_list = deserialize_list(tree_list)

    # When closing a node, do nothing else. Let function return
    elif curr_node == CLOSE_LEFT:
        #tree = deserialize_list(tree_list[1::])
        tree_list = tree_list[1::]

    elif curr_node == CLOSE_RIGHT or curr_node == CLOSE_ROOT:
        tree_list = tree_list[1::]
        # print("closing node")

    return tree, tree_list


# Converts a string int a tree
def deserialize(str_tree):

    tree = None

    # Each piece of info is separated by newlines
    tree_list = str_tree.split('\n')

    # Remove other whitespace to allow for easier parsing
    stripped_tree = [node.strip() for node in tree_list]
    # print("stripped tree: \n", stripped_tree)

    tree, tree_list = deserialize_list(stripped_tree)

    return tree


node = Node('root', Node('left', Node('left.left')), Node('right'))

serialized = serialize(node)
print("Serialized: \n", serialize(node))

deserialized = deserialize(serialized)

print("\n\nDeserialized:\n", serialize(deserialized))

assert deserialize(serialize(node)).left.left.val == 'left.left', "Doesn't work!"
