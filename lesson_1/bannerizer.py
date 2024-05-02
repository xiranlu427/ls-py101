def print_in_box(string):
    length = len(string)
    print("+" + "-" * (length + 2) + "+")
    print("|" + " " * (length + 2) + "|")
    print("| " + string + " |")
    print("|" + " " * (length + 2) + "|")
    print("+" + "-" * (length + 2) + "+")

print_in_box("")
print_in_box('To boldly go where no one has gone before.')