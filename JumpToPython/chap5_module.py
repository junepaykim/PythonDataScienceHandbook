import logging
from module import add


def main():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s: %(message)s", level=logging.NOTSET
    )
    logging.info(add(3, 4))


if __name__ == "__main__":
    main()
