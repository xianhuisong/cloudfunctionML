import pickle

# load the model from local file
clf = pickle.load(open('skt-learn-model.pkl', 'rb'))

""" return an array and each item represents the predicting result of the input data
    just get the first value
    :param:features: two dimensional array,[[1,2,3]], here we just pass one item for predicting
    :return  predicting result        
"""


def predict(features):
    return clf.predict(features)[0]
