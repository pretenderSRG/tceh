def read_file(filename):
    print(f"Read file {filename}")
    try:
        with open(filename) as f:
            return f.read()
    except IOError as e:
        print(e)


def write_data(filename, data):
    with open(filename, "w") as f:
        f.write(data)