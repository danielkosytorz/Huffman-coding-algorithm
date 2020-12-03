class Tree:
    def __init__(self, freq, char=None, left=None, right=None, leaf=False, parent=None, reset=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.leaf = leaf
        self.parent = parent
        self.reset = reset



def min_freq(trees):
    min_freq = trees[0].freq
    min_tree = trees[0]
    for tree in trees:
        if tree.freq < min_freq:
            min_freq = tree.freq
            min_tree = tree
    return min_tree

def sum_tree(tree1, tree2):
    new_freq = tree1.freq + tree2.freq
    rounded_freq = round(new_freq, 16)
    if tree1.char == None:
        return Tree(rounded_freq, left=tree1, right=tree2)
    elif tree2.char == None:
        return Tree(rounded_freq, left=tree2, right=tree1)
    else:
        if tree1.freq > tree2.freq:
            return Tree(rounded_freq, left=tree2, right=tree1)
        elif tree1.freq == tree2.freq:
            return Tree(rounded_freq, left=tree1, right=tree2)
        else:
            return Tree(rounded_freq, left=tree1, right=tree2)

def print_tree(trees):
    for tree in trees:
        print(f'{tree.char} - {tree.freq} - {tree.leaf} - {tree.parent}')
        
def remove_last(code):
    new_code = ""
    if len(code) <= 1:
        return new_code
    else:
        for i in range(len(code)-1):
            new_code += code[i]
        return new_code
    

def searching_tree(root, x):
    code = ""
    left = True
    loop = True
    while loop:
        if left:
            if root.left.leaf:
                if root.left.char == x:
                    code += "0"
                    loop = False
                else:
                    left = False
            else:
                code += "0"
                new_root = root.left
                root = new_root
        else:
            if root.right.leaf:
                if root.right.char == x:
                    code += "1"
                    loop = False
                else:
                    if root.right.reset:
                        new_root = root.parent
                        root = new_root
                        code = remove_last(code)
                    else:
                        left = True
            else:
                code += "1"
                new_root = root.right
                root = new_root
    return code





S = ['a', 'i', 's', 'd']
P = [0.1, 0.2, 0.3, 0.4]
trees = []
k = 1

for i in range(len(S)):
    trees.append(Tree(freq=P[i], char=S[i], leaf=True))

# print(f'----Stage 0----')
# print_tree(trees)

while True:
    # print(f'----Stage {k}----')
    tree1 = min_freq(trees)
    trees.pop(trees.index(tree1))
    tree2 = min_freq(trees)
    trees.pop(trees.index(tree2))
    # getting two smallest freq and suming up this to new tree and removing them from list, adding left and right attribute to new tree
    new_tree = sum_tree(tree1, tree2)
    tree1.parent = new_tree
    tree2.parent = new_tree
    new_tree.right.reset = True
    trees.append(new_tree)
    # k += 1
    # print_tree(trees)
    # print(new_tree.left.char)
    # print(new_tree.right.char)
    if new_tree.freq == 1.0:
        break
for char in S:
    x = searching_tree(trees[0], char)
    print(f'{char} - {x}')
