import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
import math
import sys
from pathlib import Path

from keras.models import Sequential, Model, model_from_json
from keras.layers import Input, Dense, Lambda, Layer
from keras import backend as K
from keras import metrics
from keras.datasets import mnist

# Arguments to be given:
# 1: the text file from which data is read
# 2: The number of observations used after deictic view
# 3: Number of epochs
data = sys.argv[1] # if defined -> train
originalVars = 8
varsPerObs = 4
observations = int(sys.argv[2])
epochs = int(sys.argv[3])
makePrediction=True

# Define paths and data
MODELPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "model"))
WEIGHTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights"))
RESULTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "results"))
input_dim = originalVars + (varsPerObs * observations)
intermediate_dim_1 = 8+observations*3
intermediate_dim_2 = 8+observations*2
latent_dim = 8+observations
output_dim = input_dim - 1
modelRepresentation = "-"+str(observations)+"-"+str(input_dim)+"-"+str(intermediate_dim_1)+"-"+str(intermediate_dim_2)+"-"+str(latent_dim)
modelName = "model"+modelRepresentation+".json"
weightsName = "weights"+modelRepresentation+".h5"
resultsName = "weights"+modelRepresentation+".txt"
DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data", "preprocessed", data))
if os.path.exists(DATAPATH) and data !="" :
    train = True
else: train = False

batch_size = 1
epsilon_std = 1.0
printTraining=1

# Read or create the model
if Path(os.path.join(MODELPATH,modelName)).exists() :
    json_file = open(os.path.join(MODELPATH,modelName), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
else:
    model = Sequential()
    model.add(Dense(intermediate_dim_1, input_dim=input_dim, activation='sigmoid'))
    model.add(Dense(intermediate_dim_2, activation='sigmoid'))
    model.add(Dense(latent_dim, activation='sigmoid'))
    model.add(Dense(intermediate_dim_2, activation='sigmoid'))
    model.add(Dense(intermediate_dim_1, activation='sigmoid'))
    model.add(Dense(output_dim, activation='sigmoid'))

    model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])

    model_json = model.to_json()
    # Modelname: model-observations.json
    with open(os.path.join(MODELPATH, modelName), "w") as json_file:
        json_file.write(model_json)

# Set weights if already existing
if Path(os.path.join(WEIGHTSPATH,weightsName)).exists() :
    model.load_weights(os.path.join(WEIGHTSPATH, weightsName))

if train:
    model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])
    text_file = open(DATAPATH, "r")
    lines = text_file.readlines()
    # Create the training data
    # Empty data object
    input_dim = originalVars + (varsPerObs * observations)
    output_dim = input_dim - 1
    inputData = np.zeros((math.floor(len(lines)/(observations+3)), input_dim), dtype=np.float64)
    outputData = np.zeros((math.floor(len(lines)/(observations+3))-1, output_dim), dtype=np.float64)

    # Remove unnecessary '\n'
    for i in range(0, len(lines)) :
        if lines[i].endswith("\n"):
                lines[i] = lines[i][:-1]

    # Fill in input and output
    # 0: gameScore
    # 1: avatarSpeed
    # 2: avatarHealthPoints
    # 3: currentAvatarOrientation-width
    # 4: currentAvatarOrientation-height
    # 5: currentAvatarPosition-width
    # 6: currentAvatarPosition-height
    # 7+4*i: observation category
    # 8+4*i: observation x-coordinate
    # 9+4*i: observation y-coordinate
    # 10+4*i: Euclidian distance to avatar
    # 10+4*max(i)+1: action (input only)
    for i in range(0,len(lines),observations+3):
        iteration = int((i / (observations + 3)))
        objects = lines[i+1].split(";")
        inputData[iteration][len(inputData[iteration])-1]=objects[len(objects)-1]
        objects = objects[0:len(objects)-1]
        inputData[iteration][0:len(objects)]=objects[0:len(objects)]
        for j in range(0,observations):
            obsObjects = lines[i+2+j].split(";")
            inputData[iteration][(len(objects)+(j*4)+0):(len(objects)+(j*4)+4)] = obsObjects[0:4]
        if iteration>0:
            outputData[iteration-1][0:(len(objects)+observations*4)]=inputData[iteration][0:(len(objects)+observations*4)]
    inputData = inputData[0:len(inputData)-1]

    model.fit(inputData, outputData, epochs=epochs, batch_size=batch_size, verbose=printTraining)

    model.save_weights(os.path.join(WEIGHTSPATH,weightsName))
else:
    np.set_printoptions(precision=16, linewidth=1000)
    weightsFile = open(os.path.join(RESULTSPATH,resultsName), "w")
    for i in range(0, len(model.layers)):
        totalWeights = np.insert(model.layers[i].get_weights()[0], 0, model.layers[i].get_weights()[1], axis=0)
        for j in range(0, len(totalWeights)):
            weightsFile.write(str(totalWeights[j].tolist())+"\n")
        weightsFile.write("\n")



if makePrediction:
    test = np.zeros((1,originalVars+observations*varsPerObs), dtype=np.float64)
    text_file = open(os.path.join(DATAPATH, "0_0.txt"), "r")
    lines = text_file.readlines()
    # Create the training data
    # Empty data object
    input_dim = originalVars + (varsPerObs * observations)

    # Remove unnecessary '\n'
    for i in range(0, len(lines)) :
        if lines[i].endswith("\n"):
                lines[i] = lines[i][:-1]

    for i in range(0,len(lines),len(lines)):
        iteration = int((i / (observations + 3)))
        objects = lines[i+1].split(";")
        test[iteration][len(test[iteration])-1]=objects[len(objects)-1]
        objects = objects[0:len(objects)-1]
        test[iteration][0:len(objects)]=objects[0:len(objects)]
        for j in range(0,observations):
            obsObjects = lines[i+2+j].split(";")
            test[iteration][(len(objects)+(j*4)+0):(len(objects)+(j*4)+4)] = obsObjects[0:4]

    print(model.predict(test, 1, 1))
