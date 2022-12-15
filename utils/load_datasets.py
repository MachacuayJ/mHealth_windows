import pandas as pd


def load_mHealth(subjects=False):
    if subjects:
        df = []
        for i in range(1, 11):
            tmp = pd.read_csv("datasets/mHealth/mHealth_subject{}.csv".format(i),
                              sep="\t", header=None)
            tmp = tmp[[14,15,16,17,18,19,20,21,22,23]]
            tmp = tmp[tmp[23] != 0]
            df.append(tmp)
    else:
        df = pd.read_csv("datasets/mHealth/mHealth_subject1.csv", sep="\t", header=None)
        for i in range(2, 11):
            df = pd.concat([df, pd.read_csv("datasets/mHealth/mHealth_subject{}.csv".format(i),
                                            sep="\t", header=None)])
        df = df[[14,15,16,17,18,19,20,21,22,23]]
        df = df[df[23] != 0]
    return df
