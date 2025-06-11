import random
import matplotlib.pyplot as plt
from collections import defaultdict
plt.switch_backend('tkagg')


# Dice roll generator
def dice_roll_generator(n):
    for _ in range(n):
        yield random.randint(1, 6)

# Simulate and plot dice rolls
def simulate_and_plot(n_rolls, seed=40):
    random.seed(seed)
    counts = defaultdict(int)

    for roll in dice_roll_generator(n_rolls):
        counts[roll] += 1

    results = [counts[i] for i in range(1, 7)]

    # Plot
    plt.figure(figsize=(6, 4))
    plt.bar(range(1, 7), results, color="mediumslateblue", edgecolor="black")
    plt.title(f"{n_rolls} Dice Rolls (Seed={seed})")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.xticks(range(1, 7))
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    plt.savefig(f"dice_rolls_{n_rolls}.png")
    print(f"Saved: dice_rolls_{n_rolls}.png")