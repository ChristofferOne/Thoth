import os
from ..Models.NetworkModel import NetworkModel
from definitions import ROOT_DIR

class ModelController:
    @staticmethod
    def listModels():
        print("Thoth")

    @staticmethod
    def getModel(name):
        if os.path.exists(ROOT_DIR+"/Storage/Networks/"+name):
            model = NetworkModel(name)
            return model
        else:
            return None

    @staticmethod
    def makeModel(name, inputs, outputs=1):
        # Set a 24x24 (576) input model
        return NetworkModel.createModel(name, inputs, outputs)
