from ModelController import ModelController

class TrainingController:
    model = None

    def __init__(self, model):
        self.selectModel(model)

    def selectModel(self, model):
        model = ModelController.getModel(model)
        self.model = model