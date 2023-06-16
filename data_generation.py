import numpy as np
import time

start = time.time()

# Define Inputs:
runs = 6000  # Anzahl der neuen Eingaben
y = 1  # Lade alte Werte -> deaktivieren für die Initialisierung oder nach dem Löschen der Dateien

# Definiere die Form des Arrays
database = np.empty((runs, 3))

# Generiere zufällige Werte
for i in range(np.shape(database)[0]):
    database[i, 0] = np.round(np.random.uniform(1, 10), decimals=2)  # x
    database[i, 1] = np.round(np.random.uniform(1, 10), decimals=2)  # y
    database[i, 2] = database[i, 0] * database[i, 0] + database[i, 1] * 2  # z = x² + y*2

print(database)

quote = 0

if y == 1:
    database_old = np.genfromtxt("database.csv", delimiter=",")
    database = np.vstack((database_old, database))

np.savetxt("database.csv", database, delimiter=",")

end = time.time()

print(f"Die Datenbank hat {np.shape(database)[0]} Zeilen.")
print(f"Die benötigte Zeit beträgt {end - start} Sekunden.")