import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42,
                   4, 99, 102, 110, 120, 121, 122, 130,
                   111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
#ids = [x for x in range(len(population_ages))]

bins = range (0, 131, 10)

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
