import os
import json
import random
from NeuronModel import NeuronModel
from definitions import ROOT_DIR


class NetworkModel:
    name = None
    inputs = None
    outputs = None
    layers = []

    def __init__(self, name):
        self.name = name
        with open(ROOT_DIR + "/Storage/Networks/" + self.name + "/model.json") as networkJsonFile:
            networkJson = json.load(networkJsonFile)
            for layer in networkJson["layers"]:
                neurons = []
                for neuron in layer["neurons"]:
                    neurons.append(NeuronModel(neuron))
                self.layers.append(neurons)
            self.inputs = len(self.layers[0][0].getWeights())
            self.outputs = len(self.layers[-1])

    def getInputsCount(self):
        return self.inputs

    def getOutputsCount(self):
        return self.outputs

    def saveModel(self):
        networkModel = {}
        layers = []
        for layer in self.layers:
            neurons = []
            for neuron in layer:
                neurons.append(neuron.getWeights())
            layers.append({"neurons": neurons})
        networkModel["layers"] = layers
        with open(ROOT_DIR + "/Storage/Networks/" + self.name, "w") as networkJsonFile:
            json.dump({networkModel}, networkJsonFile)

    @staticmethod
    def createModel(name, inputs, outputs):
        """
        :param name: String
        :param inputs: [Int, Int, ...] Int as number of neurons
        :param outputs: Int
        :return: Bool
        """
        if os.path.exists(ROOT_DIR + "/Storage/Networks/" + name):
            return False
        else:
            try:
                os.makedirs(ROOT_DIR + "/Storage/Networks/" + name)
                jsonFile = open(ROOT_DIR + "/Storage/Networks/" + name + "/model.json", "w")

                networkModel = {}
                layers = []
                i = 0
                for layer in inputs:
                    if i == 0:
                        i += 1
                        continue
                    neurons = []
                    for y in range(0, layer):
                        neuron = []
                        for z in range(0, inputs[i-1]):
                            neuron.append(random.uniform(0, 1))
                        neurons.append(neuron)
                    layers.append({"neurons": neurons})
                    i += 1

                neurons = []
                for x in range(0, outputs):
                    neuron = []
                    for z in range(0, inputs[-1]):
                        neuron.append(random.uniform(0, 1))
                    neurons.append(neuron)
                layers.append({"neurons": neurons})

                networkModel["layers"] = layers
                json.dump(networkModel, jsonFile)
            except OSError as e:
                print(e)
            return True
