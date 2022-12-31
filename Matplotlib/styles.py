import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()


if __name__ == "__main__":
    main()
