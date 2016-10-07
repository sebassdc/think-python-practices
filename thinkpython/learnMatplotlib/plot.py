
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x1 = [1, 2, 3]
x2 = [10, 14, 12]
plt.plot(x, y, label='First line')
plt.plot(x, y, label='Second line')

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it Out')
plt.legend()
plt.show()