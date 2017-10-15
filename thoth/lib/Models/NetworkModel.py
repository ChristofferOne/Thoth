import os
import json
import random
from NeuronModel import NeuronModel
from definitions import ROOT_DIR

class NetworkModel:
    name = None
    layers = []

    def __init__(self, name):
        self.name = name
        with open(ROOT_DIR+"/Storage/Networks/"+self.name+"/model.json") as networkJsonFile:
            networkJson = json.load(networkJsonFile)
            for layer in networkJson["layers"]:
                neurons = []
                for neuron in layer["neurons"]:
                    neurons.append(NeuronModel(neuron))
                self.layers.append(neurons)

    def saveModel(self):
        networkModel = {}
        layers = []
        for layer in self.layers:
            neurons = []
            for neuron in layer:
                neurons.append(neuron.getWeights())
            layers.append({"neurons": neurons})
        networkModel["layers"] = layers
        with open(ROOT_DIR+"/Storage/Networks/"+self.name, "w") as networkJsonFile:
            json.dump({networkModel}, networkJsonFile)

    @staticmethod
    def createModel(name, inputs, outputs):
        if os.path.exists(ROOT_DIR+"/Storage/Networks/"+name):
            return False
        else:
            try:
                os.makedirs(ROOT_DIR+"/Storage/Networks/"+name)
                jsonFile = open(ROOT_DIR+"/Storage/Networks/"+name+"/model.json", "w")
                networkModel = {}
                # TODO: Add support to choose layers and layer inputs/outputs
                layers = []
                # TODO: Add additonal loop on layer count
                neurons = []
                for x in range(0, inputs):
                    neuron = []
                    for z in range(0, inputs):
                        neuron.append(random.uniform(0, 1))
                    neurons.append(neuron)
                layers.append({"neurons": neurons})
                networkModel["layers"] = layers
                json.dump(networkModel, jsonFile)
            except OSError as e:
                print(e)
            return True
