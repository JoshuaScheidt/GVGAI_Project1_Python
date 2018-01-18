import json
import numpy as np
import os
import math
import sys

# Calculates the difference between the current state and any of the other possible states
def iterateDifCurrentNext(curJsonObject, actionsPerformed):
    if mainKeys[0] in curJsonObject:
        nextJsonObject = curJsonObject[mainKeys[0]]
        variance = np.var(np.concatenate((getFlatObject(curJsonObject["state"]), getFlatObject(nextJsonObject["state"]))), axis=0)
        file.write("Variance between actionset "+str(np.delete(actionsPerformed,0))+" and performing "+str(mainKeys[0])+" gives a summed variance of " +str(np.sum(variance))+".\n")
        iterateDifCurrentNext(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[0], dtype=np.str).reshape((1,1))), axis=1))
    if mainKeys[1] in curJsonObject:
        nextJsonObject = curJsonObject[mainKeys[1]]
        variance = np.var(np.concatenate((getFlatObject(curJsonObject["state"]), getFlatObject(nextJsonObject["state"]))), axis=0)
        file.write("Variance between actionset "+str(np.delete(actionsPerformed,0))+" and performing "+str(mainKeys[1])+" gives a summed variance of " +str(np.sum(variance))+".\n")
        iterateDifCurrentNext(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[1], dtype=np.str).reshape((1,1))), axis=1))
    if mainKeys[2] in curJsonObject:
        nextJsonObject = curJsonObject[mainKeys[2]]
        variance = np.var(np.concatenate((getFlatObject(curJsonObject["state"]), getFlatObject(nextJsonObject["state"]))), axis=0)
        file.write("Variance between actionset "+str(np.delete(actionsPerformed,0))+" and performing "+str(mainKeys[2])+" gives a summed variance of " +str(np.sum(variance))+".\n")
        iterateDifCurrentNext(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[2], dtype=np.str).reshape((1,1))), axis=1))
    if mainKeys[3] in curJsonObject:
        nextJsonObject = curJsonObject[mainKeys[3]]
        variance = np.var(np.concatenate((getFlatObject(curJsonObject["state"]), getFlatObject(nextJsonObject["state"]))), axis=0)
        file.write("Variance between actionset "+str(np.delete(actionsPerformed,0))+" and performing "+str(mainKeys[3])+" gives a summed variance of " +str(np.sum(variance))+".\n")
        iterateDifCurrentNext(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[3], dtype=np.str).reshape((1,1))), axis=1))
    if mainKeys[4] in curJsonObject:
        nextJsonObject = curJsonObject[mainKeys[4]]
        variance = np.var(np.concatenate((getFlatObject(curJsonObject["state"]), getFlatObject(nextJsonObject["state"]))), axis=0)
        file.write("Variance between actionset "+str(np.delete(actionsPerformed,0))+" and performing "+str(mainKeys[4])+" gives a summed variance of " +str(np.sum(variance))+".\n")
        iterateDifCurrentNext(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[4], dtype=np.str).reshape((1,1))), axis=1))

# Calculates the variances between the n states after the current state
def iterateDifNextStates(curJsonObject, actionsPerformed):
    if any(x in mainKeys[0:4] for x in curJsonObject):
        totalChildren = np.empty((1,47), dtype=np.float32).reshape(1,47)
        usedActions = np.empty((1,1), dtype=np.str).reshape(1,1)
        if mainKeys[0] in curJsonObject:
            nextJsonObject = curJsonObject[mainKeys[0]]
            totalChildren = np.concatenate((totalChildren, getFlatObject(nextJsonObject["state"])))
            usedActions = np.concatenate((usedActions, np.array(mainKeys[0], dtype=np.str).reshape((1,1))), axis=1)
            iterateDifNextStates(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[0], dtype=np.str).reshape((1,1))), axis=1))
        if mainKeys[1] in curJsonObject:
            nextJsonObject = curJsonObject[mainKeys[1]]
            totalChildren = np.concatenate((totalChildren, getFlatObject(nextJsonObject["state"])))
            usedActions = np.concatenate((usedActions, np.array(mainKeys[1], dtype=np.str).reshape((1,1))), axis=1)
            iterateDifNextStates(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[1], dtype=np.str).reshape((1,1))), axis=1))
        if mainKeys[2] in curJsonObject:
            nextJsonObject = curJsonObject[mainKeys[2]]
            totalChildren = np.concatenate((totalChildren, getFlatObject(nextJsonObject["state"])))
            usedActions = np.concatenate((usedActions, np.array(mainKeys[2], dtype=np.str).reshape((1,1))), axis=1)
            iterateDifNextStates(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[2], dtype=np.str).reshape((1,1))), axis=1))
        if mainKeys[3] in curJsonObject:
            nextJsonObject = curJsonObject[mainKeys[3]]
            totalChildren = np.concatenate((totalChildren, getFlatObject(nextJsonObject["state"])))
            usedActions = np.concatenate((usedActions, np.array(mainKeys[3], dtype=np.str).reshape((1,1))), axis=1)
            iterateDifNextStates(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[3], dtype=np.str).reshape((1,1))), axis=1))
        if mainKeys[4] in curJsonObject:
            nextJsonObject = curJsonObject[mainKeys[4]]
            totalChildren = np.concatenate((totalChildren, getFlatObject(nextJsonObject["state"])))
            usedActions = np.concatenate((usedActions, np.array(mainKeys[4], dtype=np.str).reshape((1,1))), axis=1)
            iterateDifNextStates(nextJsonObject, np.concatenate((actionsPerformed, np.array(mainKeys[4], dtype=np.str).reshape((1,1))), axis=1))
        variance = np.var(totalChildren, axis=0)
        file.write("Summed variance between actions "+str(np.delete(usedActions, 0))+" from state "+str(np.delete(actionsPerformed, 0))+" is "+str(np.sum(variance))+"\n")


def getFlatObject(jsonState):
    flatObject= np.zeros((1, 47), dtype=np.float32)
    stateKeys = ["gameScore", "avatarHealthPoints", "avatarSpeed", "avatarOrientation", "avatarPosition",
                 "observations"]
    observationKeys = ["sqDist", "category", "position"]

    for key in stateKeys:
        if key not in jsonState:
            print("Key "+key+" not found in 'state' of json object")
            quit()

    jsonStateObservation = jsonState["observations"]
    for j in range(0, len(jsonStateObservation[0])):
        for key in observationKeys:
            if key not in jsonStateObservation[j]:
                print("Key " + key + " not found in observation index "+j+" in 'state' of json object")
                quit()

    flatObject[0][0] = jsonState[stateKeys[0]]
    flatObject[0][1] = jsonState[stateKeys[1]]
    flatObject[0][2] = jsonState[stateKeys[2]]
    flatObject[0][3] = jsonState[stateKeys[3]][0]
    flatObject[0][4] = jsonState[stateKeys[3]][1]
    flatObject[0][5] = jsonState[stateKeys[4]][0]
    flatObject[0][6] = jsonState[stateKeys[4]][1]

    for j in range(0, len(jsonStateObservation)):
        flatObject[0][7+j*4] = jsonStateObservation[j][observationKeys[0]]
        flatObject[0][8+j*4] = jsonStateObservation[j][observationKeys[1]]
        flatObject[0][9+j*4] = jsonStateObservation[j][observationKeys[2]][0]
        flatObject[0][10+j*4] = jsonStateObservation[j][observationKeys[2]][1]
    return flatObject

if __name__ == '__main__':
    varData = sys.argv[1]
    DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data", "varianceCheck", varData))

    if not os.path.exists(DATAPATH):
        print("The datafile does not exist")
        quit()

    jsonObject = json.load(open(DATAPATH))
    mainKeys = ["ACTION_USE", "ACTION_LEFT", "ACTION_RIGHT", "ACTION_DOWN", "ACTION_UP", "state"]

    print("start execution")
    VARPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "varianceResults", "Variance_"+varData))
    file = open(VARPATH, "w")
    print("Write to path: "+VARPATH)
    iterateDifNextStates(jsonObject[0], np.empty((1,1), dtype=np.str).reshape(1,1))
