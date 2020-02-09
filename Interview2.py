def group_by_owners(files):
    inverted_dict = dict()
    for key, value in files.items():
        inverted_dict.setdefault(value, list()).append(key)
    return inverted_dict
if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
