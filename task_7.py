import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


num_simulations = 100000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    total = roll_dice()
    sum_counts[total] += 1

probabilities = {k: v / num_simulations * 100 for k, v in sum_counts.items()}

for total, prob in probabilities.items():
    print(f"Сума {total}: Імовірність {prob:.2f}%")

plt.bar(probabilities.keys(), probabilities.values(), color="skyblue")
plt.xlabel("Сума")
plt.ylabel("Імовірність (%)")
plt.title("Імовірність сум при киданні двох кубиків (Метод Монте-Карло)")
plt.xticks(range(2, 13))
plt.yticks(range(0, 18, 2))
plt.grid(axis="y", linestyle="--", alpha=0.7)

x_values = list(probabilities.keys())
y_values = list(probabilities.values())
plt.plot(x_values, y_values, marker="o", color="red", linestyle="-")

plt.show()
