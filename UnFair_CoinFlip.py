# Author: Μπουικλής Άγγελος - Π2018076
import random
import csv

print("τυχαίες ρίψεις κέρματος")
value = input('Πόσες φορές να ρίξω το κέρμα?\n')
# Πόσες φορές θέλει ο Χρήστης να ρίξει το κέρμα
value = int(value)
# Ένα λεξικό για το αρχείο
freq = {'Heads': 0, 'Tails': 0}
# H random επιλέγει ισοπίθανα από τα δύο Heads ή Tails
coin = ['Heads', 'Tails']

def coin_flip():
    if random.random() < 0.8:
        return 'Heads'
    else:
        return 'Tails'

# Ρίχνουμε το κέρμα value φορές "τυχαία"
for i in range(value):
    roll = coin_flip()
    freq[roll] += 1
with open('coin_Flip.csv', 'w', newline='') as file:
    # Δημιουργία CSV αρχείου για έξοδο
    writer = csv.writer(file)
    # Εκτύπωση των αποτελεσμάτων στο CSV αρχείο
    writer.writerow(['Flip_Value', 'Frequency'])
    for roll, count in freq.items():
        writer.writerow([roll, count])