import numpy as np
from matplotlib import pyplot as plt

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

import torch.nn as nn


# Exercises related to MNIST data set

def summary_mnist(train_labels, test_labels, labels_list):
    """Return a dictionary that counts the number of samples for each possible label
    >>> summary_mnist([0, 1, 2, 2, 1, 0, 0, 0, 2], [2, 0, 1, 1], range(3))
    {'train_labels_counts': [4, 2, 3], 'test_labels_counts': [1, 2, 1]}
    """

    # Write your code here
    from collections import Counter 
    train_label_counter = Counter(train_labels)
    test_label_counter = Counter(test_labels)


  

    return { "train_labels_counts" : [train_label_counter[i] for i in labels_list],
        "test_labels_counts" : [test_label_counter[i] for i in labels_list]
  } # Edit this line to return the correct output

def build_mnist_model(hidden_size, dropout_rate=0):
    """Return a Keras model that has 1 hidden layer based on this parameter:
      - hidden_size: Size of hidden layer
    >>> model = build_mnist_model(128)
    >>> model
    Sequential(
      (0): Flatten(start_dim=1, end_dim=-1)
      (1): Linear(in_features=784, out_features=128, bias=True)
      (2): ReLU()
      (3): Linear(in_features=128, out_features=10, bias=True)
    )
    """
    # Write your code here
    

    return model

if __name__ == "__main__":
    import doctest
    doctest.testmod()