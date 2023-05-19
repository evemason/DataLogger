import matplotlib.pyplot as plt
import numpy as np

resistance_values = np.array([800, 400, 200, 100, 60, 38, 21, 12, 9, 6, 4, 3, 2, 1.6, 1.1, 0.9, 0.6])
temperature_values = np.array([-25, -12.5, 0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100, 112.5, 125, 137.5, 150, 162.5, 175])

resistance_values_new = resistance_values[:7]
temperature_values_new = temperature_values[:7]

log_res = []

log_res = np.log(resistance_values_new)

plt.plot(temperature_values_new, log_res)
plt.show()

coeff = np.polyfit(temperature_values_new, log_res, 1)
print(coeff)

xp = np.linspace(-25, 175, 100)
p = np.poly1d(coeff)

plt.plot(temperature_values_new, log_res, '.', xp, p(xp), '-')
plt.xlim(-25,80)
plt.show()