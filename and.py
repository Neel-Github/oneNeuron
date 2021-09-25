from utils.model import Perceptron
from utils.all_utils import prepare_data, save_model, save_plot
import pandas as pd
import numpy as np

<<<<<<< HEAD
def main(data, eta, epochs, filename, plotFileName):

    df = pd.DataFrame(data)
    print(df)
    X,y = prepare_data(df)

    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()

    save_model(model, filename=filename)
    save_plot(df, plotFileName, model= model)
    #Actual changes done

if __name__ == '__main__':  #<< Entry point\
    
    AND = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,0,0,1],
    }
    ETA = 0.3 # 0 and 1
    EPOCHS = 10
    
    main(data=AND, eta=ETA, epochs=EPOCHS, filename = "and.model", plotFileName = "and.png")

# if __name__ == '__main__':
#     AND = {
#         "x1": [0,0,1,1],
#         "x2": [0,1,0,1],
#         "y": [0,0,0,1],
#     }
#     ETA = 0.3 # 0 and 1
#     EPOCHS = 10
#     main(data=AND, modelName="and.model", plotName="and.png", eta=ETA, epochs=EPOCHS)
=======

AND = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,0,0,1],
}

df = pd.DataFrame(AND)
print(df)


X,y = prepare_data(df)

ETA = 0.3 # 0 and 1
EPOCHS = 10

model = Perceptron(eta=ETA, epochs=EPOCHS)
model.fit(X, y)

_ = model.total_loss()

save_model(model, filename="and.model")
save_plot(df, file_name="and.png", model= model)
#Actual changes done
>>>>>>> 697dca70be383f86172b909b13618153363167e9
