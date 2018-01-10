import os
import math
import sys
from qLearner import Qlearner
from encoderGeneralFunctions import readJsonData, readFolderData, loadModel, loadModelWeights
from pathlib import Path

from keras.models import Sequential
from keras.layers import Dense

# Arguments to be given:
# 1: The model specifications (numbers after model- or weights-)
# 2: The file from which predictions must be made
# Example input: "_48s_38s_28s_18s_28s_38s_47_mean_squared_error_adam" "0_1.txt"
modelSpecs = sys.argv[1]  # if defined -> train
predictionData = sys.argv[2]
DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data", "preprocessed", predictionData))

if(DATAPATH[len(DATAPATH)-4:len(DATAPATH)] ==".txt"):
    (inputObject, outputObject) = readJsonData(DATAPATH)
elif Path(DATAPATH).exists():
    (inputObject, outputObject) = readFolderData(DATAPATH)
else:
    print("The given data file is neither a text file nor an existing folder")

# Define paths and data
RESULTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "QVals"))
resultsName = "QValues"+modelSpecs+".txt"

model = loadModel(modelSpecs)
loadModelWeights(modelSpecs, model)

if os.path.exists(DATAPATH):
    halfModel = Sequential()
    for i in range(1, len(model.layers)):
        if i == 1:
            halfModel.add(Dense(model.layers[i].input_shape[1],
                                input_dim=model.layers[0].input_shape[1],
                                activation=model.layers[i-1].activation,
                                weights=model.layers[i-1].get_weights()))
        else:
            halfModel.add(Dense(model.layers[i].input_shape[1],
                                activation=model.layers[i-1].activation,
                                weights=model.layers[i-1].get_weights()))
        if model.layers[i].input_shape[1] == 3:
            break

    predictions = halfModel.predict(inputObject, batch_size=1, verbose=1)

    weightsFile = open(os.path.join(RESULTSPATH, resultsName), "w")
    for i in range(0, len(predictions)):
        weightsFile.write(str(predictions[i].tolist()))

    # Qlearner = Qlearner(len(predictions[0]))
    # for i in range(0, len(predictions)):
    #     Qlearner.qLearning(predictions[i], inputObject[i][0])
    # Qlearner.saveQ(os.path.abspath(os.path.join(RESULTSPATH, resultsName)))
    # print("send data:")
    # print("State:")
    # print(predictions[0])
    # print("Reward:")
    # print(inputObject[0][0])
    # for i in range(0, len(predictions)):
    #     run(predictions[i], inputData[i][0])
    # save()
else:
    print("The data from which predictions must be made does not exist")