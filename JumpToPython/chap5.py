import logging


class Calculator:
    def __init__(self):
        self.result = 0
        logging.info("Calc created")

    def add(self, num):
        self.result += num
        return self.result


def main():
    calc1 = Calculator()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s: %(message)s", level=logging.NOTSET
    )
    main()
