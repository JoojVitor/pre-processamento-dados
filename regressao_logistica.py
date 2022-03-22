from sklearn import linear_model

from utilities import visualize_classifier


def logistic_regression(X, y):
    # Create the logistic regression classifier
    classifier = linear_model.LogisticRegression(solver='liblinear', C=1)

    # Train the classifier
    classifier.fit(X, y)

    # Visualize the performance of the classifier
    visualize_classifier(classifier, X, y)
