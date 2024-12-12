#!/usr/bin/env python3

# =============================================================================
# region Check out:
# https://www.geeksforgeeks.org/single-layer-perceptron-in-tensorflow/
# =============================================================================

# =============================================================================
# region Imports
# =============================================================================

import numpy as np  # NumPy is the fundamental package for scientific computing with Python.
import tensorflow as tf  # TensorFlow is an open source machine learning library
from tensorflow import (
    keras,
)  # Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow.
import matplotlib.pyplot as plt  # Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

# =============================================================================
# region Entry Point for the Script
# =============================================================================


def run():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    print(len(x_train))
    print(len(x_test))
    print(x_train[0].shape)
    plt.imshow(x_train[0])
    plt.savefig("output/img.png")
