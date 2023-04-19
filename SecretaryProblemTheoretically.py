import numpy as np
import matplotlib.pyplot as plt


def P(R, N):
	return R/N * sum([1/(n-1) for n in range(R+1, N+1)])


def compare_strategies_theoretically(n_start=2, n_stop=100, n_step=1):
	Ns = np.arange(n_start, n_stop + 1, n_step)
	Ropt = np.zeros(Ns.shape)
	Popt = np.zeros(Ns.shape)
	for i, N in enumerate(Ns):
		Ps = np.array([P(R, N) for R in range(1, N+1)])
		Ropt[i] = np.argmax([P(R, N) for R in range(1, N+1)])
		Popt[i] = Ps[int(Ropt[i])]

	plt.plot(Ns, np.array([1/n for n in Ns]), 'r--', label='Random strategy')
	plt.plot(Ns, Popt, 'g-', label='Optimal strategy')
	plt.plot(Ns, (1/np.e) * np.ones(Ns.shape), 'b:', label='Asymptotic probability of success')
	plt.grid(axis = 'both')
	plt.xlabel('Number of variants (n)')
	plt.ylabel('Probability of choosing the best variant')
	plt.legend()
	plt.savefig('Plots/Theoretical.png')
	plt.show()


if __name__ == '__main__':
	compare_strategies_theoretically(n_start=2, n_stop=75, n_step=1)
