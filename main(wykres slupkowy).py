import matplotlib.pyplot as plt
import numpy as np

names='Niemcy', 'Francja', 'Włochy', 'Hiszpania', 'Polska', 'Rumunia', 'Holandia', 'Belgia', 'Grecja', 'Czechy', 'Portugalia', 'Szwecja', 'Węgry', 'Austria', 'Bułgaria', 'Dania', 'Finlandia', 'Słowacja', 'Irlandia', 'Chorwacja', 'Litwa', 'Słowenia', 'Łotwa', 'Estonia', 'Cypr', 'Luksemburg', 'Malta'
y = [3134070, 2228857, 1672438, 1113851, 424269, 169578, 697219, 421611, 175888, 174412, 184931, 462057, 112399, 349344, 47364, 276805, 214062, 80958, 265835, 45557, 38637, 39769, 25021, 20916, 17901, 54195, 9989]
mln = np.arange(len(y))
pozycja = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
plt.bar(mln, y, color='red')
plt.subplots_adjust(left=0.02, right=1)

plt.xticks(pozycja, names)
plt.show()