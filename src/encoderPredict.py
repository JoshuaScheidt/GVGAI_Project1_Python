import os
import sys
import math
from pathlib import Path
from encoderGeneralFunctions import readJsonData, loadModel, loadModelWeights, readFolderFileNames
import numpy as np

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
    (fileNames) = readFolderFileNames(DATAPATH)
else:
    print("The given data file is neither a text file nor an existing folder")

# Define paths and data
MODELPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "model"))
WEIGHTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights"))
modelName = "model"+modelSpecs+".json"
weightsName = "weights"+modelSpecs+".h5"

model = loadModel(modelSpecs)
loadModelWeights(modelSpecs, model)

if os.path.exists(DATAPATH) and DATAPATH[len(DATAPATH)-4:len(DATAPATH)] ==".txt":
    predictions = model.predict(inputObject, batch_size=1, verbose=1)
    totalSSE=0
    maxSSE=0
    for i in range(0, len(outputObject)-1):
        print("Actual ouput state:")
        print(outputObject[i+1])
        print("Predicted output state:")
        print(predictions[i])
        SSE = 0
        for j in range(0, len(outputObject[i])):
            SSE += math.pow((predictions[i][j]-outputObject[i][j]),2)
        # print("Squared sum of errors between actual and predicted output: "+str(SSE))
        if SSE > maxSSE:
            maxSSE = SSE
        totalSSE+=SSE
    outputVar = np.var(outputObject, axis=0)
    predictionVar = np.var(predictions, axis=0)
    varDifference = outputVar-predictionVar
    print()
    print("Maximum SSE occurred: "+str(maxSSE))
    print("Total SSE: "+str(totalSSE))
    print("Variance output object: "+str(outputVar))
    print("Variance predicted object: "+str(predictionVar))
    print("")
elif os.path.exists(DATAPATH):
    # PREDICTIONPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "predictionResults", "Prediction"+modelSpecs+"-"+predictionData+".txt"))
    # file = open(PREDICTIONPATH, "w")
    # file.write("Game: "+str(predictionData)+"\n")
    for k in range(0, len(fileNames)):
        PREDICTIONPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "predictionResults", "Prediction"+modelSpecs+"-"+predictionData+"-"+str(fileNames[k])))
        file = open(PREDICTIONPATH, "w")
        file.write("Game: "+str(predictionData)+"\n")

        (inputObject, outputObject) = readJsonData(os.path.abspath(os.path.join(DATAPATH, str(fileNames[k]))))
        file.write("File: "+str(fileNames[k])+"\n")
        predictions = model.predict(inputObject, batch_size=1, verbose=1)
        totalSSE = 0
        maxSSE = 0
        for i in range(0, len(outputObject) - 1):
            file.write("Actual ouput state iteration "+str(i)+":\n")
            file.write(str(outputObject[i + 1]))
            file.write("\n")
            file.write("Predicted output state:\n")
            file.write(str(predictions[i]))
            file.write("\n")
            SSE = 0
            for j in range(0, len(outputObject[i])):
                SSE += math.pow((predictions[i][j] - outputObject[i][j]), 2)
            file.write("Squared sum of errors between actual and predicted output: "+str(SSE)+"\n\n")
            if SSE > maxSSE:
                maxSSE = SSE
            totalSSE += SSE
        outputVar = np.var(outputObject, axis=0)
        predictionVar = np.var(predictions, axis=0)
        varDifference = outputVar - predictionVar
        file.write("\n")
        file.write("\nMaximum SSE occurred: " + str(maxSSE))
        file.write("\nTotal SSE: " + str(totalSSE))
        file.write("\nVariance output object: \n" + str(outputVar))
        file.write("\nVariance predicted object: \n" + str(predictionVar))

        # file.write("\n\n\n")
        file.close()
        print("Written data to file: "+ str(PREDICTIONPATH) )
    # file.close()
    # print("Written data to file: "+ str(PREDICTIONPATH) )
else:
    print("No predictions could be made")