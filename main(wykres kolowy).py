import matplotlib.pyplot as plt
import numpy as np

names='SPD', 'CDU/CSU', 'Greens', 'FDP', 'AFD', 'Left Party', 'Others'
y = np.array([25.7, 24.1, 14.8, 11.5, 10.3, 4.9, 8.6])

plt.pie(y, autopct='%1.2f%%')
plt.legend(title="Wybory do Bundestagu 2021", labels=names)
plt.show()