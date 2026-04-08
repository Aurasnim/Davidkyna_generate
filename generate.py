
import numpy as np

np.random.seed(42)

# — Задание 1: Равномерное —

a, b = 3, 12

print("=== РАВНОМЕРНОЕ U[3; 12] ===\n")
for n in [25, 100, 500, 1000]:
    data = np.random.uniform(a, b, n)
    print(f'n = {n}:')
# Печатаем по 10 чисел в строке
for i in range(0, n, 10):
    chunk = data[i:i+10]
    print("  ","  ".join(f'{x:.4f}' for x in chunk))
print()

# — Задание 2: Рэлея —

sigma = 1.5

np.random.seed(123)

print("=== РЭЛЕЯ σ = 1.5 ===\n")
for n in [25, 100, 500, 1000]:
    data = np.random.rayleigh(sigma, n)
    print(f'n = {n}:')
for i in range(0, n, 10):
    chunk = data[i:i+10]
    print("  ", "  ".join(f'{x:.4f}' for x in chunk))
print()