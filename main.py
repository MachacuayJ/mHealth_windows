from preprocessing import time_window, handcrafted_features
from utils.functions import *
from utils.load_datasets import load_mHealth
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Specify window arguments')
parser.add_argument('-ws', '--window_size', type=int,
                    help='Samples per window')
parser.add_argument('-ov', '--overlapping', type=float,
                    help='Percentage of samples (in %) between previous and current window.')
parser.add_argument('-c', '--by_client', default=False,
                    action='store_true',
                    help='Return data by clients (True or False)')

args = parser.parse_args()

overlapping = args.overlapping/100
window_size = args.window_size

print(overlapping)
print(window_size)
print(args.by_client)

if args.by_client:
    dataset = load_mHealth(subjects=True)
    for c, dataset_subject in enumerate(dataset):
        windowed_data, window_labels = time_window(np.array(dataset_subject), window_size, overlapping)
        features = handcrafted_features(windowed_data, [mean, var, std, min, max, median, sem])
        np.save("mHealth_features_S{}.npy".format(c + 1), features)
        np.save("mHealth_labels_S{}.npy".format(c + 1), window_labels)
else:
    dataset = np.array(load_mHealth())
    windowed_data, window_labels = time_window(dataset, window_size, overlapping)
    features = handcrafted_features(windowed_data, [mean, rango, std, max, min])
    np.save("mHealth_features.npy", features)
    np.save("mHealth_labels.npy", window_labels)
