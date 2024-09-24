#Voglio realizzare un semplice calcolatore che permette di ottenere plot della distribuzione binomiale con parametri configurabili

#In sostanza, una variabile o processo può essere definito binomiale se rispetta i criteri:
#1)il risultato di ogni evento può essere considerato di due sole tipologie (successo/fallimento)
#2)eventi indipendenti
#3)la probabilità di successo/fallimento di ogni evento è costante

#p probabilità successo, 1-p probabilità fallimento, n numero di tentativi, x numero di successi
############################################################################################################

import math #for factorial
import matplotlib.pyplot as plt #per gli istogrammi

#funzione
def binomiale(n, x, p):
	base= math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
	risultato= base*p**(x)*(1-p)**(n-x)
	return risultato
	

risultati=[]
for x in range(1,21):
	risultati.append(binomiale(20, x, 0.5))
	print(x, ": binomiale =", binomiale(20, x, 0.5))
	
#creo l'istogramma 
plt.scatter(range(1, 21), risultati, color='blue')
plt.xlabel('Numero successi')
plt.ylabel('Probabilità')
#plt.axvline(media, color='b', linestyle='dashed', linewidth=1) #linea della media
plt.show()  # Mostro l'istogramma



