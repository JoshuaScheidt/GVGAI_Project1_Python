import os
import sys
import json
from pathlib import Path
import math
from encoderGeneralFunctions import readJsonData, loadModel, loadModelWeights, readFolderData
from keras.models import Model
from keras.layers import Input, Dense, Activation, Lambda
import numpy as np
from keras import backend as K
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.callbacks import History

# Arguments to be given:
# 1: the text file from which data is read
# 2: Number of epochs
# Example input: "0_1.txt" 1000
data = sys.argv[1]
epochs = int(sys.argv[2])

# Receive input/output data
DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data", "preprocessed", data))

if(DATAPATH[len(DATAPATH)-4:len(DATAPATH)] ==".txt"):
    (inputObject, outputObject) = readJsonData(DATAPATH)
elif Path(DATAPATH).exists():
    (inputObject, outputObject) = readFolderData(DATAPATH)
else:
    print("The given data file is neither a text file nor an existing folder")

# Define paths and data
MODELPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "model"))
WEIGHTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights"))
HISTORYPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "history"))

# Define model representation
dimensions = [
    len(inputObject[0]),
    # 43,
    38,
    # 33,
    28,
    # 23,
    18,
    # 13,
    8,
    3,
    8,
    # 13,
    18,
    # 23,
    28,
    # 33,
    38,
    # 43,
    len(outputObject[0])
]
activations = ["sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid"]
loss = "mean_squared_error"
optimizer = "adam"

modelRepresentation = "_"+data+"_varAuto_"
for i in range(0, len(dimensions)-1):
    modelRepresentation = modelRepresentation+str(dimensions[i])+activations[i][0]+"_"
modelRepresentation = modelRepresentation+str(dimensions[len(dimensions)-1])+"_"+loss+"_"+optimizer

# Read or create the model
if Path(os.path.join(MODELPATH, "model"+modelRepresentation+".json")).exists():
    model = loadModel(modelRepresentation)
else:
    batch_size = 1
    input_dim = len(inputObject[0])
    output_dim = len(outputObject[0])
    n_h1 = 38
    n_h2 = 28
    n_h3 = 18
    n_h4 = 8
    n_lat = 3
    n_h5 = 8
    n_h6 = 18
    n_h7 = 28
    n_h8 = 38
    epsilon_std = 1.0
    nb_epoch = 100

    x = Input(shape=(input_dim,))
    h = Dense(n_h1, activation='sigmoid')(x)
    h = Dense(n_h2, activation='sigmoid')(h)

    z_mean = Dense(n_z)(h)
    z_log_sigma = Dense(n_z)(h)


    def sampling(args):
        z_mean, z_log_sigma = args
        epsilon = K.random_normal(K.shape(z_mean),
                                  mean=0., std=epsilon_std)
        return z_mean + K.exp(z_log_sigma) * epsilon


    z = Lambda(sampling, output_shape=(n_z,))([z_mean, z_log_sigma])

    d = Dense(n_h2, activation='relu')(z)
    d = Dense(n_h1, activation='relu')(d)
    x_decoded_mean = Dense(original_dim, activation='sigmoid')(d)

    # end-to-end autoencoder
    model = Model(x, x_decoded_mean)

    # encoder, from inputs to latent space
    encoder = Model(x, z_mean)


    def vae_loss(x, x_decoded_mean):
        xent_loss = K.binary_crossentropy(x, x_decoded_mean)
        kl_loss = - 0.5 * K.mean(1 + z_log_sigma - K.square(z_mean) - K.exp(z_log_sigma), axis=-1)
        return xent_loss + kl_loss


    model.compile(optimizer='rmsprop', loss=vae_loss)

    model_json = model.to_json()
    with open(os.path.join(MODELPATH, "model"+modelRepresentation+".json"), "w") as json_file:
        json_file.write(model_json)

# Set weights if already existing
if Path(os.path.join(WEIGHTSPATH, "weights"+modelRepresentation+".h5")).exists():
    loadModelWeights(modelRepresentation, model)

if os.path.exists(DATAPATH):
    history = History()

    model.compile(loss=loss, optimizer=optimizer, metrics=["accuracy"])

    model.fit(inputObject, outputObject, epochs=epochs, batch_size=1, verbose=1, callbacks=[history])

    model.save_weights(os.path.join(WEIGHTSPATH, "weights"+modelRepresentation+".h5"))

    if Path(os.path.join(HISTORYPATH, "history"+modelRepresentation+".json")).exists():
        with open(os.path.join(HISTORYPATH, "history" + modelRepresentation + ".json"), "a") as json_file:
            json.dump(history.history, json_file)
    else:
        with open(os.path.join(HISTORYPATH, "history"+modelRepresentation+".json"), "w") as json_file:
            json.dump(history.history, json_file)
else:
    print("The given data does not exist in '\\res\\data\\preprocessed\\...'")
