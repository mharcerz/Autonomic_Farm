import pandas as pd  # data processing
import numpy as np  # working with arrays
import matplotlib.pyplot as plt  # visualization
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.tree import plot_tree  # tree diagram


def classify_action_words(X):
    i_counter = 0
    ii_counter = 0
    for i in X:
        for ii in i:
            if ii == 'zasiane':
                X[i_counter][ii_counter] = 0
            elif ii == 'nie_zasiane':
                X[i_counter][ii_counter] = 1
            elif ii == 'rosnie':
                X[i_counter][ii_counter] = 0
            elif ii == 'wyroslo':
                X[i_counter][ii_counter] = 1
            elif ii == 'potrzebny_srodek_owady':
                X[i_counter][ii_counter] = 0
            elif ii == 'niepotrzebny_srodek_owady':
                X[i_counter][ii_counter] = 1
            elif ii == 'sa_chwasty':
                X[i_counter][ii_counter] = 0
            elif ii == 'brak_chwastow':
                X[i_counter][ii_counter] = 1
            elif ii == 'kwasowa':
                X[i_counter][ii_counter] = 0
            elif ii == 'w_normie':
                X[i_counter][ii_counter] = 1
            elif ii == 'zasadowa':
                X[i_counter][ii_counter] = 2
            ii_counter += 1

    return X


def make_decision(field):
    attributes = [field.sianie, field.czy_rosnie, field.suchosc_gleby, field.owady, field.chwasty, field.ph_gleby]
    attributes = np.array(attributes)
    attributes_shaped = np.reshape(attributes, (1, 6))

    attributes_changed = classify_action_words(attributes_shaped)

    decision = model.predict(attributes_changed)
    return decision