import numpy as np
# import pickle
import math
import random

#Input would be array, have to split 
#Input = Array of states(activations and actions), put for-loop around it. Also contains reward
# Let's rework 

class Qlearner():
    alpha = 0.1
    gamma = 0.9
    lambda_ = 0.9
    #dont know how to properly init this
    oldCoordinate=0
    firstCoordinate = True
    #has to be initialized in a proper way
    discretiseConstant=1000
    dimensions=0
    EPSILON = 10e-16
    
    qTable = np.empty([1])
    #np.random.rand(discretiseConstant, discretiseConstant, discretiseConstant)*1e-4 #maybe 1e-5
    
    def __init__(self, dimensions):
        self.dimensions=dimensions
        self.makeShape()
        self.oldCoordinate=np.zeros((dimensions, 1), dtype=np.int16)
        # print(self.qTable)
        # print(np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)))
        # print(self.qTable[0][np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).tolist()])
        # print("...")
    
    def makeShape(self):
        dimCount=self.dimensions
        dim = []
        for i in range(self.dimensions):
            dim.append(self.discretiseConstant)
        dimTuple= tuple(dim)
        self.qTable = np.ndarray(shape=(dimTuple), dtype=np.float32, order='F')

    def updateQValue(self, coord, reward):
        #update Q-Value
        if self.firstCoordinate:
            self.oldCoordinate = coord
            self.firstCoordinate = False
            if self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int16).tolist()]<self.EPSILON and self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int16).tolist()]>-self.EPSILON:
                self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate), 1)).astype(np.int16).tolist()] = (random.random()-0.5)/50
        else:
            #not the max value, just use the Qvalue for the next state
            # qTableOldCoordinate = self.qTable
            # qTableNewCoordinate = self.qTable
            # for i in range(0, len(self.oldCoordinate)):
            #     qTableOldCoordinate = qTableOldCoordinate[int(self.oldCoordinate[i])]
            #     qTableNewCoordinate = qTableNewCoordinate[int(coord[i])]
# print(self.oldCoordinate)
# print(np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(int).tolist())
# print(self.qTable[0][np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int8).tolist()])
# print(self.qTable[0][np.reshape(coord, (len(coord),1)).astype(np.int8).tolist()])
# self.qTable[0][0][0][0] = 1
# print(self.qTable[0][0][0][0])
            if self.qTable[np.reshape(coord, (len(coord),1)).astype(np.int16).tolist()]<self.EPSILON and self.qTable[np.reshape(coord, (len(coord),1)).astype(np.int16).tolist()]>-self.EPSILON:
                self.qTable[np.reshape(coord, (len(coord), 1)).astype(np.int16).tolist()] = (random.random()-0.5)/50

            self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate), 1)).astype(np.int16).tolist()] = self.alpha*(reward+self.gamma*self.qTable[np.reshape(coord, (len(coord),1)).astype(np.int16).tolist()]-self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int16).tolist()])
            # self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int16).tolist()]+=self.alpha*(reward+self.gamma*self.qTable[np.reshape(coord, (len(coord),1)).astype(np.int16).tolist()]- self.qTable[np.reshape(self.oldCoordinate, (len(self.oldCoordinate),1)).astype(np.int16).tolist()])
            self.oldCoordinate = coord	# Should we do e(s,a)?
        
    def qLearning(self, coord, reward):
# print(coord)
# print(reward)
        mappedCoord= self.mapCoordinate(coord)
        self.updateQValue(mappedCoord, reward)
        
    def mapCoordinate(self, coordinate):
        for i in range(0, len(coordinate)):
            coordinate[i] = int(math.floor(coordinate[i]*self.discretiseConstant))
        return coordinate
        
    def saveQ(self, location):
        f = open(location,"w")
        list = np.zeros((self.dimensions, 1), dtype=np.int16)
        # print(list)
        # print(list[0])
        # quit()

        f.write("[")
        for i in range(0, len(self.qTable)):
            print(i)
            f.write("[")
            for j in range(0, len(self.qTable[i])):
                f.write("[")
                for k in range(0, len(self.qTable[i][j])):
                    f.write(str(self.qTable[i][j][k]))
                    if k < self.discretiseConstant-1:
                        f.write(",")
                f.write("]")
            f.write("]\n")
        f.write("]")

        # np.set_printoptions(threshold=math.pow(self.discretiseConstant, self.dimensions), linewidth=100000, formatter={'all':lambda x:str(x)+","})
        # output = self.qTable.
        # output = self.recursion(list, 0,"")
        # f.write(np.array2string(self.qTable).replace(" ", ""))
        f.close
  
    def recursion(self, list, counter, output):
        # if counter == 0:
        #     print(counter)
        # if counter<self.dimensions-1:
        #     for i in range(self.discretiseConstant):
        #         output+="["
        #         list[counter] = i
        #         self.recursion(list, counter+1, output)
        #         output+="]"
        # else:
        #     for i in range(self.discretiseConstant):
        #         output+="["
        #         list[counter] = i
        #         output+=str(self.qTable[0][list.tolist()])
        #         output+="]"
        #
        # if len(list)==0:
        #     return output
        result = ""

        np.set_printoptions(precision=np.float32, threshold=math.pow(self.discretiseConstant, self.dimensions))


        return result