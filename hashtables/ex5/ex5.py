# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for file in files:
        split = file.split('/')[-1]
        if split not in cache:
            cache[split] = [file]
        else:
            cache[split].append(file)
    for file in queries:
        if file in cache:
            result += cache[file]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
