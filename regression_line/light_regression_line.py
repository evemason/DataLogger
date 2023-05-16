import matplotlib.pyplot as plt
import numpy as np

current_values = np.array([7, 17, 22, 30, 40, 47, 50, 60, 70, 78, 150, 210, 300, 380, 440, 500, 600])
illuminance = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800])

log_current = []
log_light = []
for i in range(len(current_values)):
    current_log_value = np.log(current_values[i])
    light_log_value = np.log(illuminance[i])
    log_current.append(current_log_value)
    log_light.append((light_log_value))

plt.plot(log_light, log_current)
plt.show()

coeff = np.polyfit(log_light, log_current, 1)

print(coeff)

xp = np.linspace(0, 10, 100)
p = np.poly1d(coeff)

plt.plot(log_light, log_current, '.', xp, p(xp), '-')
plt.xlim(0,10)
plt.show()

