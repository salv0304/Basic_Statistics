#con numpy è possibile ottenere quanto fatto molto rapidamente e con meno codice

import matplotlib.pyplot as plt #per gli istogrammi
import numpy as np

risultati= np.random.randint(1,7, 100) #minore, maggiore, numero di estrazioni
print(risultati)

media= np.mean(risultati)
dev_std= np.std(risultati)
print("Media =", media, "\n Dev_Stand =", dev_std)

#creo l'istogramma 
plt.hist(risultati, bins=range(1, 8), color='r', edgecolor='black', align='left')
plt.xlabel('Valore del dado')
plt.ylabel('Frequenza')
plt.axvline(media, color='b', linestyle='dashed', linewidth=1) #linea della media
plt.show()  # Mostro l'istogramma

#########################################
#per truccare il dado
#values = [1, 2, 3, 4, 5, 6]
#probs = [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]
#sample = np.random.choice(values, p=probs)
