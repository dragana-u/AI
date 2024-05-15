import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    # Vashiot kod tuka
    col_index = int(input())
    broj_drva = int(input())
    kriterium = input()
    za_klasifikacija = [int(i) for i in input().split(" ")]

    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    train_X_2 = list()
    for t in train_X:
        row = [t[i] for i in range(len(t)) if i != col_index]
        train_X_2.append(row)
    test_X_2 = list()
    for t in test_X:
        row = [t[i] for i in range(len(t)) if i != col_index]
        test_X_2.append(row)
    za_klasifikacija = [za_klasifikacija[i] for i in range(len(za_klasifikacija)) if i != col_index]

    classifier = RandomForestClassifier(n_estimators=broj_drva, criterion=kriterium, random_state=0)
    classifier.fit(train_X_2, train_Y)

    predictions = classifier.predict(test_X_2)
    accuracy = accuracy_score(test_Y, predictions)
    print(f'Accuracy: {accuracy}')
    predicted_class = classifier.predict([za_klasifikacija])[0]
    print(predicted_class)
    verojatnosti = classifier.predict_proba([za_klasifikacija])[0]
    print(verojatnosti)
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    train_X = train_X_2
    test_X = test_X_2
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
