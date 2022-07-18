import matplotlib.pyplot as plt
import numpy as np


def _plot_temps(data_file):
    """Plot my weight."""
    with open(data_file, "r") as data_lines:
        data_lines = data_lines.readlines()
        x_data = [float(line.split(" ")[2]) for line in data_lines]
        y_data = [float(line.split(" ")[1]) for line in data_lines]
        dates = [line.split(" ")[0] for line in data_lines]
    plt.grid()
    plt.plot(x_data, y_data)
    plt.axhline(33.5, color="r")
    plt.scatter(x_data, y_data)
    plt.ylim(25, 35)
    plt.title("Temperature in V's Hot Box Flat")
    plt.xlabel("18 July 2022: Hours minutes")
    plt.ylabel("Temperature deg C")
    plt.xticks(x_data, dates, rotation='45', fontsize=10)
    plt.annotate("max = 33.5C", xy=(1, 33.5), xytext=(1, 33.8), color="r")
    plt.tight_layout()
    # plt.show()
    plt.savefig("temps_18-07-2022.png")
    plt.close()


if __name__ == '__main__':
    _plot_temps("home_18-07-2022.txt")
