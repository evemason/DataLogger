import matplotlib.pyplot as plt
import numpy as np

resistance_values = np.array([800, 400, 200, 100, 60, 38, 21, 12, 9, 6, 4, 3, 2, 1.6, 1.1, 0.9, 0.6])
temperature_values = np.array([-25, -12.5, 0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100, 112.5, 125, 137.5, 150, 162.5, 175])

log_res = []
for i in range(len(resistance_values)):
    value = np.log(resistance_values[i])
    log_res.append(value)


plt.plot(temperature_values, log_res)
plt.show()

coeff = np.polyfit(temperature_values, log_res, 2)
print(coeff)

xp = np.linspace(-25, 175, 100)
p = np.poly1d(coeff)

plt.plot(temperature_values, log_res, '.', xp, p(xp), '-')
plt.xlim(-25,175)
plt.show()