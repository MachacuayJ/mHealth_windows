import numpy as np


def time_window(data, window_size, overlapping=0.5, label_index=-1):
    """
    param data: Numpy array of shape (n_records, dim)
    param window_size: Size of the time windows
    param overlapping: % of records (0-1) included from the previous time window in the current window
    param label_index: column index where the label is.
    return: Numpy array of shape (n_windows, size, dim), Numpy array of labels of each window
    WARNINGS:
    * If the data is not size-compatible with the desired time window size, the last records will be omitted.
    * If the overlapping is not compatible with the window_size parameter, then the least integer will be considered.
        For instance: Given window_size=3 and overlapping=0.5, the number of records from the previous window will be 1.
    """
    if label_index == -1:
        label_index = data.shape[1]-1
    feature_index = [i for i in range(data.shape[1]) if i != label_index]

    windows = []
    window_labels = []

    classes = np.unique(data[:, label_index])
    prev_rec = int(overlapping * window_size)

    for given_class in classes:
        sub_data = data[data[:, label_index] == given_class]
        c = 0
        while c+window_size < sub_data.shape[0]:
            window = sub_data[c:c + window_size, feature_index]
            windows.append(window)
            window_labels.append(sub_data[c+window_size-1, label_index])
            c += window_size - prev_rec

    return np.array(windows), np.array(window_labels)


def handcrafted_features(windows, functions):
    """
    param windows: Numpy array of shape (n_windows, size, dim)
    param functions: List of functions to be applied along "size" for each window.
    return: Numpy array of shape (n_windows, len(functions)*dim)
    """
    n_windows = windows.shape[0]
    dim = windows.shape[2]
    features = np.zeros((n_windows, len(functions)*dim))
    d = 0
    for function in functions:
        for i in range(n_windows):
            window = windows[i]
            feature = np.apply_along_axis(function, 0, window)
            features[i][d:d+dim] = feature
        d += dim
    return features
