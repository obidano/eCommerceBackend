import os


def createFolders(list_path):
    for path in list_path:
        if not os.path.isdir(path):
            os.mkdir(path)
