import os
import sys
import math
from encoderGeneralFunctions import readJsonData, loadModel, loadModelWeights

# Arguments to be given:
# 1: The model specifications (numbers after model- or weights-)
# 2: The file from which predictions must be made
# Example input: "_48s_38s_28s_18s_28s_38s_47_mean_squared_error_adam" "0_1.txt"
modelSpecs = sys.argv[1]  # if defined -> train
predictionData = sys.argv[2]

DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data", "preprocessed", predictionData))
(inputObject, outputObject) = readJsonData(DATAPATH)

# Define paths and data
MODELPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "model"))
WEIGHTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights"))
modelName = "model"+modelSpecs+".json"
weightsName = "weights"+modelSpecs+".h5"

model = loadModel(modelSpecs)
loadModelWeights(modelSpecs, model)

if os.path.exists(DATAPATH) and predictionData != "":
    predictions = model.predict(inputObject, batch_size=1, verbose=1)
    for i in range(0, len(inputObject)):
        print("Actual input:")
        print(inputObject[i])
        print("Predicted output of next iteration:")
        print(predictions[i])
        SSE = 0
        for j in range(0, len(inputObject[i])-1):
            SSE += math.pow((predictions[i][j]-inputObject[i][j]),2)
        print("Squared sum of errors: "+str(SSE))
else:
    print("The data from which predictions must be made does not exist")