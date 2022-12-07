with open('input7.txt') as f:
    lines = f.readlines()


class Directory:
    name = ""
    parent = None
    children = None
    size = 0

    def __init__(self, name, p):
        self.name = name
        self.parent = p
        if self.parent:
            if not self.parent.children:
                self.parent.children = []
            self.parent.children.append(self)

    def get_size(self):
        sum_of_children = 0
        if self.children:
            for child in self.children:
                sum_of_children += child.get_size()
        return self.size + sum_of_children


root = Directory("/", None)
cd = root
for line in lines:
    if line[0] == "$":
        if "cd" in line:
            directory = line.split(" ")[2].strip("\n")
            if directory != "/":
                if directory == "..":
                    if cd.parent:
                        cd = cd.parent
                    else:
                        cd = root
                else:
                    for d in cd.children:
                        if d.name == directory:
                            cd = d
    else:
        if "dir" in line.split(" ")[0]:
            directory = line.split(" ")[1].strip("\n")
            found = False
            if cd.children:
                for d in cd.children:
                    if d.name == directory:
                        found = True
            if not found:
                new_dir = Directory(directory, cd)
        else:
            cd.size += int(line.split(" ")[0])


size = root.get_size() if root.get_size() <= 100000 else 0


def get_reasonable_size(parent):
    global size
    if parent.children:
        for child in parent.children:
            get_reasonable_size(child)
    size += parent.get_size() if parent.get_size() <= 100000 else 0


for c in root.children:
    get_reasonable_size(c)

print(size)

