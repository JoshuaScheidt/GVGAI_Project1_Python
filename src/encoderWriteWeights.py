import numpy as np
import os
import sys
import math
from encoderGeneralFunctions import loadModel, loadModelWeights

# Arguments to be given:
# 1: The model specifications (numbers after model- or weights-)
# Example input: "48s_38s_28s_18s_28s_38s_47_mean_squared_error_adam"
modelSpecs = sys.argv[1]  # if defined -> train

model = loadModel(modelSpecs)
loadModelWeights(modelSpecs, model)

# Define paths and data
RESULTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "results"))
resultsName = "weights"+modelSpecs+".txt"

np.set_printoptions(precision=16, linewidth=1000)
weightsFile = open(os.path.join(RESULTSPATH, resultsName), "w")
for i in range(0, len(model.layers)):
    if model.layers[i].use_bias:
        totalWeights = np.insert(model.layers[i].get_weights()[0], 0, model.layers[i].get_weights()[1], axis=0)
    else:
        totalWeights = model.layers[i].get_weights()[0]

    for j in range(0, len(totalWeights)):
        weightsFile.write(str(totalWeights[j].tolist())+"\n")
    weightsFile.write("\n")
