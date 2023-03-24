import re


if __name__ == '__main__':
    name_pattern = r"My name is .*\."
    is_name = re.match(name_pattern, "My name is Serg.")
    print(is_name)
    