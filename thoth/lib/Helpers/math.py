from numpy import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


def sigmoid_derivate(x):
    return x * (1 - x)