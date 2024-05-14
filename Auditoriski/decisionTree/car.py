import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset


if __name__ == '__main__':
    dataset = read_file("car.csv")

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    test_set = dataset[int(0.7 * len(dataset)):]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x, train_y)
    print(f'Depth: {classifier.get_depth()}\n')
    print(f'Leaves: {classifier.get_n_leaves()}\n')

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1
    accuracy = accuracy / len(test_set)
    print(f'Accuracy: {accuracy}\n')
    features_importances = list(classifier.feature_importances_)
    print(f'Feature importances: {features_importances}')
    most_important_feature = features_importances.index(max(features_importances))
    least_important_feature = features_importances.index(min(features_importances))
    print(f'Most important feature: {most_important_feature}')
    print(f'Least important feature: {least_important_feature}')

    train_x_2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(row)

    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(row)
    # ponatamu e isto kako pogore


