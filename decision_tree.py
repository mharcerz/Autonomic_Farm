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

fname = Path("resources/training_tree/tree.sav")

if fname.exists():
    model = pickle.load(open(fname, 'rb'))
else:
    print("------------------------")
    print("Building Tree")
    print("------------------------")
    df = pd.read_csv('resources/training_tree/training_tree.csv')

    for i in df.sianie.values:
        if i == 'zasiane':
            df.sianie.replace(i, 0, inplace=True)
        elif i == 'nie_zasiane':
            df.sianie.replace(i, 1, inplace=True)

    for i in df.czy_rosnie.values:
        if i == 'rosnie':
            df.czy_rosnie.replace(i, 0, inplace=True)
        elif i == 'wyroslo':
            df.czy_rosnie.replace(i, 1, inplace=True)

    for i in df.owady.values:
        if i == 'potrzebny_srodek_owady':
            df.owady.replace(i, 0, inplace=True)
        elif i == 'niepotrzebny_srodek_owady':
            df.owady.replace(i, 1, inplace=True)

    for i in df.chwasty.values:
        if i == 'sa_chwasty':
            df.chwasty.replace(i, 0, inplace=True)
        elif i == 'brak_chwastow':
            df.chwasty.replace(i, 1, inplace=True)

    for i in df.ph_gleby.values:
        if i == 'kwasowa':
            df.ph_gleby.replace(i, 0, inplace=True)
        elif i == 'w_normie':
            df.ph_gleby.replace(i, 1, inplace=True)
        elif i == 'zasadowa':
            df.ph_gleby.replace(i, 2, inplace=True)

    X = df.copy()
    y = X.pop('decyzja')

    model = dtc(criterion='entropy', max_depth=8)

    # model.fit(X, y) generuje warning w predict
    # https://stackoverflow.com/questions/69326639/sklearn-warning-valid-feature-names-in-version-1-0

    model.fit(X.values, y)

    features_name = df.columns[:-1]

    target_names = ['nawoz', 'osusz', 'pestycydy', 'podlej', 'pomin', 'zasiej', 'zbierz',
                    'zerwij_chwasty']

    plot_tree(model,
              feature_names=features_name,
              class_names=target_names,
              filled=True,
              rounded=True)

    # now, before saving to file:
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(8, 6)
    # when saving, specify the DPI
    plt.savefig("resources/training_tree/myplot.png", dpi=700)

    pickle.dump(model, open(fname, 'wb'))
