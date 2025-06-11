from advanced_reader import AdvancedReader
from decorator import colorize
from dice_simulation import simulate_and_plot

@colorize("cyan")
def show_combined(text):
    print(text)

if __name__ == "__main__":
    adv = AdvancedReader("files/input1.txt")
    combined = adv.combine_files(["files/input1.txt", "files/input2.txt"])
    show_combined(combined)

    for rolls in [10, 100, 1000, 10000]:
        simulate_and_plot(rolls)