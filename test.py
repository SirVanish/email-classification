import cPickle as c
from train import genDict

# will load the classifier .mdl file
def load(classifier):
    with open(classifier) as fp:
        clf = c.load(fp)
    return clf

# load the classifier
clf = load("email-classifier.mdl")
# generate the dictionary
d = genDict()

while True:
    # generate a features list
    features = []
    # obtain input from user
    input = raw_input("> ").split()
    if input[0] == "exit":
        break

    # for every word in the dictionary, we'll count it's occurances
    # from our input string
    for word in d:
        features.append(input.count(word[0]))

    # stores the classifier's predictions in a list of lists of features
    result = clf.predict([features])

    # print 'spam' or 'not spam' based on results
    print ["Not Spam", "Spam"][result[0]]
