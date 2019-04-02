# Email-Classification
An email classifier for clssifying spam vs non-spam emails.


Written in Python. Uses the Naive Bayes approach for text classification. Also uses a very basic approach to machine learning and data mining.


This was a small project I worked on in order to teach myself the following concepts:
  - Text Classification
  - Machine Learning
  - Data Mining
  - Naive Bayes Classification

Some of the resources I used are:
  - Reference videos. [Part 1](https://www.youtube.com/watch?v=xm-wmBwJLww) and [Part 2](https://www.youtube.com/watch?v=6Wd1C0-3RXM).
  - [Email datasets](https://www.youtube.com/redirect?q=http%3A%2F%2Fwww.aueb.gr%2Fusers%2Fion%2Fdata%2Fenron-spam%2Fpreprocessed%2Fenron1.tar.gz&redir_token=igZge-rUVimppzb4E5XF1o5v9ih8MTU1NDI2NzgyNEAxNTU0MTgxNDI0&event=video_description&v=xm-wmBwJLww)
  
**If code fails to run because of missing scikit-learn(sklearn) libray**, then try running:

for `pip`:

`pip install -U scikit-learn`

for `conda`:

`conda install scikit-learn`

On the Python Console.

## Using 'train.py' nad 'test.py'
Running 'train.py'

e.g. `python train.py` will run the training and generation of the 'email-classifier.mdl' using the dataset from the 'emails/' directory.

Afterwards, running 'test.py'

e.g. `python test.py` will allow user to input messages to test whether they're or not they're considered email spams using the classifier generated from the training.
