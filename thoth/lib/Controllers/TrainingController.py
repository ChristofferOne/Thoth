from ModelController import ModelController
from ..TrainingModels.TrainingModelResolver import TrainingModelResolver
from numpy import exp

class TrainingController:
    model = None

    def __init__(self, model):
        self.selectModel(model)

    def selectModel(self, model):
        model = ModelController.getModel(model)
        self.model = model
        print(self.model.getInputsCount())
        print(self.model.getOutputsCount())

    @staticmethod
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    @staticmethod
    def __sigmoid_derivate(self, x):
        return x * (1 - x)

    def train(self):
        trainingModelData = TrainingModelResolver.getImageModel(self.model.name)
        trainingLoops = input("Training loops (Int):")

        for iteration in xrange(trainingLoops):
            print("Starting training")
            # Remove this
            # Start training sequence