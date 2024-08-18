import numpy as np
import matplotlib.pyplot as plt

n_simulations = 1000000

dice1 = np.random.randint(1, 7, size=n_simulations)
dice2 = np.random.randint(1, 7, size=n_simulations)

sums = dice1 + dice2

sum_values, counts = np.unique(sums, return_counts=True)
probabilities = counts / n_simulations

analytic_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

analytic_probs = np.array([analytic_probabilities[i] for i in sum_values])


plt.figure(figsize=(10, 6))
plt.bar(sum_values - 0.2, probabilities, width=0.4, label='Monte Carlo', color='blue', align='center')
plt.bar(sum_values + 0.2, analytic_probs, width=0.4, label='Аналітичні', color='orange', align='center')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності випадання сум при киданні двох кубиків')
plt.xticks(sum_values)
plt.legend()
plt.grid(True)
plt.show()

for sum_value, prob, anal_prob in zip(sum_values, probabilities, analytic_probs):
    print(f"Сума: {sum_value}, Монте-Карло: {prob:.5f}, Аналітична: {anal_prob:.5f}")