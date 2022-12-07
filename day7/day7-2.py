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

deletable = []


def get_reasonable_size(parent, diff_required):
    global size
    if parent.children:
        for child in parent.children:
            get_reasonable_size(child, diff_required)
    if parent.get_size() >= diff_required:
        deletable.append(parent.get_size())


capacity = 70000000
target = 30000000
current = root.get_size()
diff = capacity - current
diff_to_target = target - diff
print(diff_to_target)

for c in root.children:
    get_reasonable_size(c, diff_to_target)

deletable.sort()
print(deletable)


