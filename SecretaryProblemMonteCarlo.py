from random import shuffle, choice
import numpy as np
import matplotlib.pyplot as plt


def random_strategy(n, trials) -> float:
	count = 0
	choices = np.arange(1, n+1)
	for trial in np.arange(trials):
		chosen = choice(choices)
		if chosen == n:
			count += 1
	return count / trials


def optimal_strategy(n, trials) -> float:
	count = 0
	choices = np.arange(1, n+1)
	reject_to = round(n / np.e)
	for trial in np.arange(trials):
		shuffle(choices)
		cur_max = np.max(choices[:reject_to])
		for variant in choices[reject_to:]:
			if variant > cur_max:
				if variant == n:
					count += 1
				break
	return count / trials


def compare_strategies_monte_carlo(trials=1e4, n_start=2, n_stop=100, n_step=1):
	random_probs = []
	optimal_probs = []
	ns = np.arange(n_start, n_stop + 1, n_step)
	for n in ns:
			random_prob, optimal_prob = random_strategy(n, trials), optimal_strategy(n, trials)
			random_probs.append(random_prob)
			optimal_probs.append(optimal_prob)

	plt.plot(ns, random_probs, 'r--', label='Random strategy')
	plt.plot(ns, optimal_probs, 'g-', label='Optimal strategy')
	plt.plot(ns, (1/np.e) * np.ones(ns.shape), 'b:', label='Asymptotic probability of success')
	plt.grid(axis = 'both')
	plt.xlabel('Number of variants (n)')
	plt.ylabel('Probability of choosing the best variant')
	plt.legend()
	plt.savefig('Plots/MonteCarlo.png')
	plt.show()


if __name__ == '__main__':
	compare_strategies_monte_carlo(trials=1e5, n_start=2, n_stop=75, n_step=1)
	