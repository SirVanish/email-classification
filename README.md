# Email-Classification
An email classifier for clssifying spam vs non-spam emails.


Written in Python. Uses the Naive Bayes approach for text classification. Also uses a very basic approach to machine learning and data mining.


This was a small project I worked on in order to teach myself the following concepts:
  - Text Classification
  - Machine Learning
  - Data Mining
  - Naive Bayes Classification

Some of the resources I used are:
  - Reference videos. [Part 1](https://www.youtube.com/watch?v=xm-wmBwJLww) and [Part 2](https://www.youtube.com/watch?v=6Wd1C0-3RXM). (Credits to Sourav Johar)
  - [Email datasets](https://www.youtube.com/redirect?q=http%3A%2F%2Fwww.aueb.gr%2Fusers%2Fion%2Fdata%2Fenron-spam%2Fpreprocessed%2Fenron1.tar.gz&redir_token=igZge-rUVimppzb4E5XF1o5v9ih8MTU1NDI2NzgyNEAxNTU0MTgxNDI0&event=video_description&v=xm-wmBwJLww). (Credits to enron1)
  
**If code fails to run because of missing scikit-learn(sklearn) libray**, then try running:

for `pip`:

`pip install -U scikit-learn`

for `conda`:

`conda install scikit-learn`

On the Python Console.

## Using 'train.py' nad 'test.py'
Running 'train.py'

e.g. `python train.py` will run the training and generation of the 'email-classifier.mdl' using the dataset from a 'emails/' directory (dataset I used can be obtained from the link above).
![train sample image](https://raw.githubusercontent.com/SirVanish/email-classification/master/images/train_sample_img.png)

Afterwards, running 'test.py'

e.g. `python test.py` will allow user to input messages to test whether messages are or aren't considered email spams using the classifier generated from the training. To exit the input, type `exit`.
![test sample image](https://raw.githubusercontent.com/SirVanish/email-classification/master/images/test_sample_img.png)

Keep in mind that this was just a little fun learning project that I built and wanted to reference in the future, etc. And that the **text classifier is not perfect**! To get the perfect classifier, one needs to use *tons* of data. I used a *very small* sample of data!
