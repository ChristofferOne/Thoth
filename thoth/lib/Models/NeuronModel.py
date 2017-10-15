class NeuronModel:
    weights = []

    def __init__(self, weights):
        self.weights = weights

    def getWeights(self):
        return self.weights