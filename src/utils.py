import numpy as np
import matplotlib.pyplot as plt


def train_test_data(seq, steps):
    X, Y = list(), list()
    for i in range(len(seq)):
        sample = i + steps
        if sample > len(seq)-1:
            break
        x, y = seq[i:sample],seq[sample]
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def train_test_validation_plot(train_size, test_size):
    plt.figure(figsize=(12,9))
    plt.plot(data_daily[:train_size])
    plt.plot(data_daily[train_size:test_size])
    plt.plot(data_daily[test_size:])