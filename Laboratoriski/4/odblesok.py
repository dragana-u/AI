import os
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    procent_podelba = int(input())
    kriterium = input()

    encoder = OrdinalEncoder()
    encoder.fit([red[:-1] for red in dataset])

    train_set = dataset[int((100 - procent_podelba) / 100 * len(dataset)):]
    train_X = [red[:-1] for red in train_set]
    train_Y = [red[-1] for red in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[:int((100 - procent_podelba) / 100 * len(dataset))]
    test_X = [red[:-1] for red in test_set]
    test_Y = [red[-1] for red in test_set]
    test_X = encoder.transform(test_X)

    classifier = DecisionTreeClassifier(criterion=kriterium, random_state=0)
    classifier.fit(train_X, train_Y)
    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')
    accuracy = accuracy_score(test_Y, classifier.predict(test_X))
    print(f'Accuracy: {accuracy}')
    features = list(classifier.feature_importances_)
    print(f'Most important feature: {features.index(max(features))}')
    print(f'Least important feature: {features.index(min(features))}')
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)