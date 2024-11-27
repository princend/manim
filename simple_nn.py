from tensorflow import keras

model =keras.Sequential()
input_layer = keras.layers.Dense(units=3, 
                                 activation='relu')
model.add(input_layer)
hidden_layer = keras.layers.Dense(units=4, 
                                  activation='relu')
model.add(hidden_layer)
output_layer = keras.layers.Dense(units=1, 
                                  activation='sigmoid')
model.add(output_layer)