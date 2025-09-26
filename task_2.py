import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функцій і меж інтегрування
def f(x):
    return x ** 2

a = 0
b = 2

# Метод Монте-Карло
np.random.seed(42)
N = 500

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, max(f(np.linspace(a, b, 100))), N)

points_under_curve = y_rand < f(x_rand)
monte_carlo_integral = (b-a) * max(f(np.linspace(a, b, 100))) * np.sum(points_under_curve) / N
print(f"Metod Monte-Carlo: {monte_carlo_integral:.2f}")

# Перевірка аналітичного інтеграла
analytical_integral = (b**3 - a**3)/3
print(f"Analytical Integral: {analytical_integral:.2f}")

# Перевірка методом quad
result, error = spi.quad(f, a, b)
print(f"Integral (quad):  {result:.2f} +- {error:.2e}")

# Побудова графіка з точками Монте-Карло
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x^2')
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.scatter(x_rand[points_under_curve], y_rand[points_under_curve], color='green', s=10, alpha=0.6, label='Under the curve')
ax.scatter(x_rand[~points_under_curve], y_rand[~points_under_curve], color='red', s=10, alpha=0.6, label='Above the curve')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Metod Monte-Carlo for f(x) = x^2 from 0 to 2')
ax.legend()
plt.grid()
plt.show()