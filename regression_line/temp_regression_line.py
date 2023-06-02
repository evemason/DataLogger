import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


resistance_values = np.array([25872,19814, 15300, 11909, 9340, 7378, 5869, 4700, 3788, 3071, 2505, 2055, 1694, 1405, 1170])
temperature_values = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

popt, pcov = curve_fit(
    lambda t, a , b, c: a*np.exp(b*t) + c,
    resistance_values, temperature_values, p0 = (60, -0.00009, -10))

a = popt[0]
b = popt[1]
c = popt[2]

print(a)
print(b)
print(c)

plt.plot(resistance_values, temperature_values)
plt.show()

coeff = np.polyfit(resistance_values, temperature_values , 2)
print(coeff)

xp = np.linspace(1000, 25872, 1000)
yp = a * np.exp(b*xp) + c
p = np.poly1d(coeff)

#initial = 60 * np.exp(-0.00009*xp) -10


#plt.plot(xp, initial, 'k')
plt.plot(xp,yp, 'k')
plt.plot(resistance_values, temperature_values, '.', xp, p(xp), '-')
plt.xlim(1000,25872)
plt.show()