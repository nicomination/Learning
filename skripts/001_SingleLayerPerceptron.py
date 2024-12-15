#!/usr/bin/env python3

# =============================================================================
# region Check out:
# https://www.geeksforgeeks.org/single-layer-perceptron-in-tensorflow/
# =============================================================================

import numpy as np
import tensorflow as tf
from tensorflow import (
    keras,
)
import matplotlib.pyplot as plt


def run():
    # x = images, y = labels
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    print(len(x_train))
    print(len(x_test))
    print(x_train[0].shape)
    plt.imshow(x_train[0])
    plt.savefig(f"output/img{y_train[0]}.png")

    # Normalizing the dataset (0-255) to (0-1)
    x_train = x_train / 255
    x_test = x_test / 255

    # Flatting the dataset in order to compute for model building
    # reshape from 28x28 to 1x784
    x_train_flatten = x_train.reshape(len(x_train), 28 * 28)
    x_test_flatten = x_test.reshape(len(x_test), 28 * 28)

    # Building the a neural network
    # 10 = number of output nodes
    # 784 = number of input nodes
    # sigmoid = activation function
    model = keras.Sequential(
        [keras.layers.Dense(10, input_shape=(784,), activation="sigmoid")]
    )

    # Compiling the model
    # adam = optimizer
    # sparse_categorical_crossentropy = loss function
    # accuracy = metric
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    # Training the model
    # x_train_flatten = input
    # y_train = Labels
    # epochs = number of iterations
    model.fit(x_train_flatten, y_train, epochs=20)

    # Evaluating the model
    model.evaluate(x_test_flatten, y_test)

### Summary
'''
1. **Load the MNIST data and display images.**  
2. **Normalize and flatten the image data.**  
3. **Create a simple neural network with one dense layer.**  
4. **Train the model using the Adam optimizer and evaluate it with cross-entropy loss.**  
5. **Evaluate the model on the test data.**'''