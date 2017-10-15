#imports
from lib.Controllers.TrainingController import TrainingController
from lib.Controllers.ModelController import ModelController

def main():
    print("Select task")
    print("1. Train")
    print("2. Create model")
    print("3. Exit")

    action = input()
    if action == 1:
        model = raw_input("Model to train: (--list for model list)")
        if model == "--list":
            ModelController.listModels()
            model = raw_input("Select:")

        trainingController = TrainingController(model)
        if trainingController.model == None:
            print("Model can not be found")
        else:
            print()
    elif action == 2:
        name = raw_input("Name of model (q to exit):")
        inputs = input("Number of inputs:")
        outputs = input("Number of outputs:")
        if name == "q":
            main()
        else:
            newModel = ModelController.makeModel(name, inputs, outputs)
            if newModel:
                print("Model created")
            else:
                print("Model exists")
            main()
    elif action == 3:
        return None

if __name__ == "__main__":
    main()