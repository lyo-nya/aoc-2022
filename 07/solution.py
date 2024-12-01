import fileinput


class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class TreeNode(Node):
    def __init__(self, name, value, parent, children):
        self.parent = parent
        self.visited = 0
        self.children = children
        super().__init__(name, value)

    def traverse(self):
        if self.visited or not self.children:
            self.visited = 1
            return self.value
        self.visited = 1
        for child in self.children:
            child_value = child.traverse()
            self.value += child_value
        return self.value

    def traverse_dirs_ub(self, max_size):
        if not self.children:
            return []
        out = [self] if (self.value <= max_size) else []
        for child in self.children:
            out += child.traverse_dirs_ub(max_size)
        return out

    def traverse_dirs_lb(self, min_size):
        if not self.children:
            return []
        out = [self] if (self.value >= min_size) else []
        for child in self.children:
            out += child.traverse_dirs_lb(min_size)
        return out


class Tree:
    def __init__(self, root: TreeNode):
        self.current_node = root
        self.root = root
        self.current_node = root

    def up(self):
        if self.current_node.parent:
            self.current_node = self.current_node.parent

    def cd(self, name):
        if name == "..":
            self.up()
        elif name == "/":
            self.current_node = self.root
        else:
            for child in self.current_node.children:
                if child.name == name:
                    self.current_node = child

    def add(self, node: Node):
        self.current_node.children.append(node)


root = TreeNode(name="/", value=0, parent=None, children=[])
tree = Tree(root=root)

for line in fileinput.input(files="input.txt"):
    instruction = line.strip()
    if "$ cd" in instruction:
        d = instruction.split(" ")[2]
        tree.cd(d)
        continue
    if instruction == "$ ls":
        continue
    val, name = instruction.split(" ")
    if val == "dir":
        node = TreeNode(name=name, value=0, parent=tree.current_node, children=[])
        tree.add(node)
        continue
    node = TreeNode(name=name, value=int(val), parent=tree.current_node, children=[])
    tree.add(node)

tree.root.traverse()
part_1_dirs = tree.root.traverse_dirs_ub(100000)
print(f"Part 1 answer is {sum([d.value for d in part_1_dirs])}")
space_to_free_up = 30000000 - (70000000 - tree.root.value)
part_2_dirs = tree.root.traverse_dirs_lb(space_to_free_up)
print(f"Need to free up {space_to_free_up}")
print(f"Part 2 answer is {sorted(part_2_dirs, key = lambda x: x.value)[0].value}")
