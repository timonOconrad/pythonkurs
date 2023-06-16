import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Set log level to '2' (warnings and error messages)

from tensorflow import keras

# Numpy laden und festlegen des Zufalls-Startwertes
import numpy as np
np.random.seed(1337)



def share(array):
    anzahl_kleiner_werte = len([element for element in array if element < 0.1])
    anteil = (anzahl_kleiner_werte / len(array)) * 100
    return anteil

# y = x²+ b*2

# Daten in Arrays speichern
data = np.genfromtxt("database.csv", delimiter=",")

eingangswerte = data[:, :2]  # First two columns as input values
ausgangswerte = data[:, 2:]  # Last column as output values



model = keras.Sequential([
    keras.layers.Dense(8, input_dim=2, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(64, activation='sigmoid'),
    keras.layers.Dense(32, activation='sigmoid'),
    #keras.layers.Dense(1, activation='sigmoid'),
    keras.layers.Dense(1)
])

# Kompiliert das Model, damit es spaeter verwendet werden kann
model.compile(loss='mean_squared_error', optimizer='adam')

# Trainiert das Model mit den Eingangs- und den entsprechenden Ausgangswerten fuer 512 Epochen
model.fit(x=eingangswerte, y=ausgangswerte, epochs=512, batch_size=1024)

# Testet die Eingangsdaten und schreibt die Ergebnisse in die Konsole
predictions = model.predict(eingangswerte)

print(share(predictions-ausgangswerte))



#print(model.predict([[1,1.2]]))
