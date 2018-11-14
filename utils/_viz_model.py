"""
------------------------------------------------------------------
Vizualize the architecture of a sklearn network.
The network is a feedforward, fully connected neural network.
You must have keras, ann_visualizer, and graphviz installed.
------------------------------------------------------------------
"""

print(__doc__)

from keras.models import Sequential
from keras.layers import Dense
from ann_visualizer.visualize import ann_viz
from sklearn.neural_network.multilayer_perceptron import MLPClassifier, MLPRegressor


def viz_model(model):
    assert (isinstance(model, MLPClassifier) or
            isinstance(model, MLPRegressor)), \
        'Model must be a sklearn neural network!'
    network = Sequential()
    for coef in model.coefs_:
        network.add(Dense(input_dim=coef.shape[0],
                          units=coef.shape[1],
                          activation='relu',
                          kernel_initializer='uniform'))

    ann_viz(network, title="Neural Network Architecture")
