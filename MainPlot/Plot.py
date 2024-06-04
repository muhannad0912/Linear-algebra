import numpy as np
import matplotlib.pyplot as plt

# Distance traveled by robber: d = 2.5t
# Distance traveled by sheriff: du = 3(t-5)

t = np.linspace(0, 40, 1000)
d = 2.5 * t
du = 3 * (t - 5)

fig, ax = plt.subplots()
plt.title('Linear System')
plt.xlabel('time (in minutes)')
plt.ylabel('distance (in km)')
ax.set_xlim([0 , 40])
ax.set_ylim([0 , 100])

ax.plot(t, d, c='green', label='Robber')
ax.plot(t, du, c='purple', label='Sheriff')
plt.axvline(x=30 , color = "red" , linestyle = "--")
plt.axhline(y=75 , color = "red" , linestyle = "--")

plt.savefig('/workspaces/Linear-algebra/MainPlot/plot.png')
