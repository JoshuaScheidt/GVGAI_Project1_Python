import json
import numpy as np
import os
from keras.models import model_from_json
from pathlib import Path


def readJsonData(location):
    if not os.path.exists(location):
        print("The datafile does not exist")
        quit()

    jsonObject = json.load(open(location))
    keys = ["gameScore", "avatarHealthPoints", "avatarSpeed", "avatarOrientation", "avatarPosition", "observations"]
    observationKeys = ["sqDist", "category", "position"]
    totalVars = 1+1+1+2+2+10*(1+1+2)
    totalInput= np.zeros((len(jsonObject), totalVars+1), dtype=np.float64)
    totalOutput= np.zeros((len(jsonObject), totalVars), dtype=np.float64)
    wrongIndices=[]
    for i in range(0, len(jsonObject)):
        if "action" not in jsonObject[i] and "state" not in jsonObject[i] and "newState" not in jsonObject[i]:
            print("Index "+i+" does not contain action, state or newState")
            quit()

        jsonState = jsonObject[i]["state"]
        jsonNewState = jsonObject[i]["newState"]
        for key in keys:
            if key not in jsonState:
                print("Key "+key+" not found in 'state' of json object " +str(i))
                quit()
            if key not in jsonNewState:
                print("Key "+key+" not found in 'newState' of json object " +str(i))
                quit()

        jsonStateObservation = jsonState["observations"]
        jsonNewStateObservation = jsonNewState["observations"]
        for j in range(0, len(jsonStateObservation)):
            for key in observationKeys:
                if key not in jsonStateObservation[j]:
                    print("Key " + key + " not found in observation index "+j+" in 'state' of json object " + str(i))
                    quit()
        for j in range(0, len(jsonNewStateObservation)):
            for key in observationKeys:
                if key not in jsonNewStateObservation[j]:
                    print("Key " + key + " not found in observation index "+j+" in 'newState' of json object " + str(i))
                    quit()

        totalInput[i][0] = jsonState[keys[0]]
        totalOutput[i][0] = jsonNewState[keys[0]]
        totalInput[i][1] = jsonState[keys[1]]
        totalOutput[i][1] = jsonNewState[keys[1]]
        totalInput[i][2] = jsonState[keys[2]]
        totalOutput[i][2] = jsonNewState[keys[2]]
        totalInput[i][3] = jsonState[keys[3]][0]
        totalOutput[i][3] = jsonNewState[keys[3]][0]
        totalInput[i][4] = jsonState[keys[3]][1]
        totalOutput[i][4] = jsonNewState[keys[3]][1]
        totalInput[i][5] = jsonState[keys[4]][0]
        totalOutput[i][5] = jsonNewState[keys[4]][0]
        totalInput[i][6] = jsonState[keys[4]][1]
        totalOutput[i][6] = jsonNewState[keys[4]][1]

        for j in range(0, len(jsonStateObservation)):
            totalInput[i][7+j*4] = jsonStateObservation[j][observationKeys[0]]
            totalInput[i][8+j*4] = jsonStateObservation[j][observationKeys[1]]
            totalInput[i][9+j*4] = jsonStateObservation[j][observationKeys[2]][0]
            totalInput[i][10+j*4] = jsonStateObservation[j][observationKeys[2]][1]
        for j in range(0, len(jsonNewStateObservation)):
            totalOutput[i][7+j*4] = jsonNewStateObservation[j][observationKeys[0]]
            totalOutput[i][8+j*4] = jsonNewStateObservation[j][observationKeys[1]]
            totalOutput[i][9+j*4] = jsonNewStateObservation[j][observationKeys[2]][0]
            totalOutput[i][10+j*4] = jsonNewStateObservation[j][observationKeys[2]][1]
        totalInput[i][len(totalInput[i])-1] = jsonObject[i]["action"]

    return totalInput, totalOutput

def readJsonDataAutoEncode(location):
    if not os.path.exists(location):
        print("The datafile does not exist")
        quit()

    jsonObject = json.load(open(location))
    keys = ["gameScore", "avatarHealthPoints", "avatarSpeed", "avatarOrientation", "avatarPosition", "observations"]
    observationKeys = ["sqDist", "category", "position"]
    totalVars = 1+1+1+2+2+10*(1+1+2)
    totalInput= np.zeros((len(jsonObject), totalVars+1), dtype=np.float64)
    for i in range(0, len(jsonObject)):
        if "action" not in jsonObject[i] and "state" not in jsonObject[i] and "newState" not in jsonObject[i]:
            print("Index "+i+" does not contain action, state or newState")
            quit()

        jsonState = jsonObject[i]["state"]

        jsonStateObservation = jsonState["observations"]
        for j in range(0, len(jsonStateObservation)):
            for key in observationKeys:
                if key not in jsonStateObservation[j]:
                    print("Key " + key + " not found in observation index "+j+" in 'state' of json object " + str(i))
                    quit()

        totalInput[i][0] = jsonState[keys[0]]
        totalInput[i][1] = jsonState[keys[1]]
        totalInput[i][2] = jsonState[keys[2]]
        totalInput[i][3] = jsonState[keys[3]][0]
        totalInput[i][4] = jsonState[keys[3]][1]
        totalInput[i][5] = jsonState[keys[4]][0]
        totalInput[i][6] = jsonState[keys[4]][1]

        for j in range(0, len(jsonStateObservation)):
            totalInput[i][7+j*4] = jsonStateObservation[j][observationKeys[0]]
            totalInput[i][8+j*4] = jsonStateObservation[j][observationKeys[1]]
            totalInput[i][9+j*4] = jsonStateObservation[j][observationKeys[2]][0]
            totalInput[i][10+j*4] = jsonStateObservation[j][observationKeys[2]][1]

    return totalInput

def readFolderData(location):
    for file in os.listdir(location):
        if file.endswith(".txt"):
            (inputObject, outputObject) = readJsonData(os.path.abspath(os.path.join(location, file)))
            if not "totalInput" in locals():
                totalInput = inputObject
                totalOutput = outputObject
            else:
                totalInput = np.concatenate((totalInput, inputObject))
                totalOutput = np.concatenate((totalOutput, outputObject))

    return totalInput, totalOutput

def readFolderDataAutoEncode(location):
    for file in os.listdir(location):
        if file.endswith(".txt"):
            (inputObject, outputObject) = readJsonDataAutoEncode(os.path.abspath(os.path.join(location, file)))
            if not "totalInput" in locals():
                totalInput = inputObject
            else:
                totalInput = np.concatenate((totalInput, inputObject))

    return totalInput

def readFolderFileNames(location):
    for file in os.listdir(location):
        print(file)
        if file.endswith(".txt"):
            if not "fileNames" in locals():
                fileNames = [np.array(file, dtype=np.str)]
            else:
                fileNames = np.append(fileNames, [np.array(file, dtype=np.str)], axis=0)
    return fileNames

def loadModel(modelSpecs):
    MODELPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "model"))
    modelName = "model"+modelSpecs+".json"
    if Path(os.path.join(MODELPATH, modelName)).exists():
        json_file = open(os.path.join(MODELPATH, modelName), 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        return model_from_json(loaded_model_json)
    else:
        print("The given model does not exist")
        quit()


def loadModelWeights(modelSpecs, model):
    WEIGHTSPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights"))
    weightsName = "weights"+modelSpecs+".h5"
    if Path(os.path.join(WEIGHTSPATH, weightsName)).exists():
        model.load_weights(os.path.join(WEIGHTSPATH, weightsName))
    else:
        print("The given weights do not exist")
        quit()