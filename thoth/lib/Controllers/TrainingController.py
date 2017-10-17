from ModelController import ModelController
from ..TrainingModels.TrainingModelResolver import TrainingModelResolver
from ..Helpers import math

class TrainingController:
    model = None

    def __init__(self, model):
        self.selectModel(model)

    def selectModel(self, model):
        model = ModelController.getModel(model)
        self.model = model
        print(self.model.getInputsCount())
        print(self.model.getOutputsCount())

    def train(self):
        trainingModelData = TrainingModelResolver.getImageModel(self.model.name)
        trainingLoops = input("Training loops (Int):")

        for iteration in xrange(trainingLoops):
            print("Starting training")
            # Remove this
            # Start training sequence