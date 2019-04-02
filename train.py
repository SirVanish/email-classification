import os
import re
import time
from collections import Counter
# we will be using the Naive Bayes Machine Learning model for this project
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
# cPickle will be used for saving the classifier model
import cPickle as c

# used to save the classifier given a file name
def save(classifier, name):
    with open(name, "wb") as fp:
        c.dump(classifier, fp)
    print "Saved classifier as " + name

# generate a dictionary using email data samples
def genDict():
    print("Generating dictionary...")

    # directory path
    dir = "emails/"
    files = os.listdir(dir)

    # appends the directory to the file names
    emails = [dir + email for email in files]

    # words list to store the words read from emails
    words = []
    # counter to count num. of emails read
    c = 0

    for email in emails:
        # open the email and read it's contents
        f = open(email)
        contents = f.read()

        # appends the words in the email read to the words list
        words += contents.split(" ")

        if (console_log):
            # print the number of emails read
            print("read " + str(c) + " emails")
        c += 1

    # keep track of start time for dictionary generation
    start_time = time.time()

    # removes non-alphanumeric symbols from the words list
    for i in range(len(words)):
        # next line of code was unoptimized
        # words[i] = re.compile('[^a-zA-Z]').sub('', words[i])
        if not words[i].isalpha():
            words[i] = ""

    # create a dictionary with word counts using words list
    dictionary = Counter(words)
    # then delete the non-alphanumeric sumbols from the dictionary
    del dictionary[""]

    # keep track of time end time for dictionary generation
    end_time = time.time()

    # prints 3000 most commonly used words from the dictionary
    # print dictionary.most_common(3000)

    # print the time it took to generate the dictionary
    print("Generated dictionary from " + str(c) + " emails.")
    print("It took " + str(round(end_time - start_time, 2)) + "s to generate dictionary.")

    # returns 3000 most commonly used in a dictionary
    return dictionary.most_common(3000)

# generate a dataset given a dictionary
def genDataset(dictionary):
    print("\nGenerating dataset...\nThis may take some time...")

    # directory path
    dir = "emails/"
    files = os.listdir(dir)

    # appends the directory to the file names
    emails = [dir + email for email in files]

    # keep track of start time for dictionary generation
    start_time = time.time()
    # counter to count num. of emails read
    c = 0
    # append data to a feature set
    feature_set = []
    # create a list for labelling ham vs spam
    labels = []

    # read through emails
    for email in emails:
        # store dataset
        data = []
        f = open(email)
        words = f.read().split(" ")

        # count the num. of times a word occurs
        for entry in dictionary:
            data.append(words.count(entry[0]))
        # append dataset to feature feature_set
        # for every email, we convert the email to a numerical form
        # then we add it to the feature set
        feature_set.append(data)

        # label the email as ham or spam based on email's nomenclature
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)

        if (console_log):
            # print the number of emails read for dataset
            print("read " + str(c) + " emails for dataset")
        c += 1

    # keep track of time end time for dictionary generation
    end_time = time.time()
    # print time it took to generate feature set and labels
    print("Dataset generated from " + str(c) + " emails.")
    print("It took " + str(round(end_time - start_time, 2)) + "s to generate feature set and labels.")
    # return both the feature set and it's ham vs spam labels
    return feature_set, labels

def main():
    # record the total number of time it took to execute program
    total_start_time = time.time()
    # generate the dictionary
    d = genDict()
    # generate the feature set with it's ham vs spam labels
    features, labels = genDataset(d)

    # the num. of fatures and labels should equal
    # these numbers should be the same
    # print("Num. of feature sets: " + str(len(features)))
    # print("Num. of labels:" + str(len(labels)))

    # for time
    total_end_time = time.time()
    print("\nTotal time it for training data: " + str(round(total_end_time - total_start_time, 2)) + "s.")

    # tts splits the dataset into two parts (a traingin part and a testing part)
    # x_train denotes the features used for training alone
    # x_test denotes the features we'll use for testing
    # y_train denotes the labels used for training
    # y_test denotes the labels we'll use for testing
    # and test_size denotes that we'll use 80% of the dataset for trainging and
    # 20% of the dataset for our testing
    x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

    # create the classifier and fit it with the training features
    # and corresponding training labels
    classifier = MultinomialNB()
    classifier.fit(x_train, y_train)
    print("Classifier generated!")

    # make predictions based on the x_test we generated
    predictions = classifier.predict(x_test)
    # print the accuracy of our predictions using the y_test we generated
    print("Accuracy score: " + str(accuracy_score(y_test, predictions)))

    # save the classifier
    save(classifier, "email-classifier.mdl")


# for console logging of program activity
console_log = False

if __name__ == "__main__": main()
