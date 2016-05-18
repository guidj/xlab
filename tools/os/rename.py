if __name__ == "__main__":

    import os
    import os.path
    import sys

    rootdir = sys.argv[1]
    pattern = sys.argv[2]
    if len(sys.argv) > 3:
        replace = sys.argv[3]
    else:
        replace = ""

    for root, _, files in os.walk(rootdir):
        for file in files:
            if pattern in file:
                os.rename(os.path.join(root, file), os.path.join(root, file.replace(pattern, replace)))
