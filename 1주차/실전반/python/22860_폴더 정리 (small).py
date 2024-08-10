from sys import stdin


class Folder:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.children_set = set()

    def add_child(self, file):
        self.children.append(file.name)
        self.children_set.add(file.name)

    def query(self):
        return len(self.children_set), len(self.children)


class File:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name


input = stdin.readline
n, m = map(int, input().split())
folders = {"main": Folder('')}
files = []

for _ in range(n+m):
    p, f, c = input().split()
    if c == '1':
        folders[f] = Folder(p)
    else:
        files.append(File(p, f))

for name, folder in folders.items():
    if name == "main":
        folder.parent = None
    else:
        folder.parent = folders[folder.parent]

for file in files:
    folder = folders[file.parent]
    while folder is not None:
        folder.add_child(file)
        folder = folder.parent

for _ in range(int(input())):
    folder_name = input().strip().split("/")[-1]
    print(*folders[folder_name].query())