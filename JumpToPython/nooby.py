import logging


def print_vs_logging():
    logging.debug("Debug!")
    logging.info("just some info")
    logging.error("Oh~!")


def keys_indict():
    d = {i: i + 4 for i in range(4)}

    for key, val in d:
        ...


def range_len_pattern():
    a = [i for i in range(4)]
    for i, v in enumerate(a):
        print("i is {i} and v is {v}")

    b = [i + 4 for i in range(4)]

    for i, (av, bv) in enumerate(zip(a, b)):
        if av is bv:
            print("It's same")

    for av, bv in zip(a, b):
        print("It could be this way")


def checking_bool_or_len(x):
    if bool(x):
        pass
    if len(x) != 0:
        pass
    # Should not use as above
    # below is enough

    if x:
        pass


def comprehension():
    odd_squares = {i: i * i for i in range(10)}


def main():
    return


if __name__ == "__main__":
    main()
