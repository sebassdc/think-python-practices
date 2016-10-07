import matplotlib.pyplot as plt
import random

x = range(1, 9)
y = []

for i in range(len(x)):
    j = random.randrange(0, 11, 1)
    y.append(j)


plt.scatter(x, y, label='skitscat', color='k', marker='x', s=500)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
