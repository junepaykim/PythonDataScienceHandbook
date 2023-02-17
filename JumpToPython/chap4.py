def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError:
            print("Not a number!")


def newFile(*args):
    with open("NewFile.txt", "w") as f:
        f.write("\n")


def printSame():
    print("Hallo" "World")
    # "HalloWorld"
    print("Hallo", "World")
    # "Hallo World"
    print()


def add_many(*args):
    result = 0


def print_kwargs(**kwargs):
    print(kwargs)


def main():
    newFile("Hallo World!")
    bare_except()


if __name__ == "__main__":
    main()
