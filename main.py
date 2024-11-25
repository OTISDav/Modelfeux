from train import train_model
from test import test_model

if __name__ == "__main__":

    model = train_model()

    print("Test du model")
    test_model(model)


print('otis')