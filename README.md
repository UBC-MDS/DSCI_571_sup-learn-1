# DSCI 571: Supervised Learning I

Welcome to DSCI 571, an introductory supervised machine learning course! In this course we will focus on basic machine learning concepts such as data splitting, cross-validation, generalization error, overfitting, the fundamental trade-off, the golden rule, and data preprocessing. You will also be exposed to common machine learning algorithms such as decision trees, K-nearest neighbours, SVMs, naive Bayes, and logistic regression using [the scikit-learn framework](https://scikit-learn.org/stable/).

2020-21 instructor: **Varada Kolhatkar**

## Course Learning Outcomes    

By the end of the course, students are expected to be able to:
- describe supervised learning and identify what kind of tasks it is suitable for;
- explain common machine learning concepts such as classification and regression, data splitting, overfitting, parameters and hyperparameters, and the golden rule;
- identify when and why to apply data pre-processing techniques such as imputation, scaling, and one-hot encoding;
- describe at a high level how common machine learning algorithms work, including decision trees, K-nearest neighbours, and naive Bayes;
- use Python and the `scikit-learn` package to responsibly develop end-to-end supervised machine learning pipelines on real-- world datasets and to interpret your results carefully.

## Deliverables
    
The following deliverables will determine your course grade:

| Assessment       | Weight  | 
| :---:            | :---:   |
| Lab Assignment 1 | 15%     |
| Lab Assignment 2 | 15%     |
| Lab Assignment 3 | 15%     |
| Lab Assignment 4 | 15%     |
| Quiz 1           | 20%     |
| Quiz 2           | 20%     |


## Class Meetings

We will be meeting three times every week: twice for lectures and once for the lab. 

### Lecture format
 
Lectures of this course will be a combination of pre-recorded videos and class discussions and activities. You are expected to watch the videos before the lecture. We'll spend the lecture time in group activities and Q&A sessions. 


## Lecture Schedule


| Lecture  | Topic  | Datasets | Resources and optional readings |
|-------|------------|-----------|-----------|
|      | [Motivation and course information](lectures/00_motivation-course-information.ipynb) | <li>[Indian Liver Patient Records](https://www.kaggle.com/uciml/indian-liver-patient-records)</li><li>[House Sales in King County](https://www.kaggle.com/harlfoxem/housesalesprediction)</li><li>[IMDB movie reviews](https://www.kaggle.com/utathya/imdb-review-dataset)</li> | |
|   1   | [Terminology, baselines, decision trees](lectures/01_lecture-terminology-baselines-decision-trees.ipynb) | <li>[House Sales in King County](https://www.kaggle.com/harlfoxem/housesalesprediction)</li> <li>[Canada US cities toy dataset](lectures/data/canada_usa_cities.csv)</li>| |
|   2   | [ML fundamentals](lectures/02_lecture-ml-fundamentals.ipynb) | <li>[Canada US cities toy dataset](lectures/data/canada_usa_cities.csv)</li> | |
|   3   | [kNNs, SVM RBF](lectures/03_lecture-kNN-SVM-RBF.ipynb) | <li>[Canada US cities toy dataset](lectures/data/canada_usa_cities.csv)</li><li> [Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)</li>| | 
|   4   | [Preprocessing and pipelines](lectures/04_lecture-preprocessing.ipynb) |<li> [Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)</li><li>[California Housing](https://www.kaggle.com/harrywang/housing?select=housing.csv)</li>| |
|   5   | [Categorical features and text features](lectures/05_lecture-categorical-text-feats.ipynb) | <li>[The adult census dataset](https://www.kaggle.com/uciml/adult-census-income#)</li> |
|   6   | [Hyperparameter optimization, optimization bias](lectures/06_lecture-hyperparameter-optimization.ipynb) | <li>[The adult census dataset](https://www.kaggle.com/uciml/adult-census-income#)</li> |
|   7   | [Naive Bayes](lectures/07_lecture-naive-Bayes.ipynb) | <li>[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)</li>| [Conditional probability visualization](https://setosa.io/ev/conditional-probability/) |
|   8   | Logistic Regression, multi-class classification | <li>[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)</li>| |

### Installation

We are providing you with a `conda` environment file which is available [here](env-dsci-571.yaml). You can download this file and create a conda environment for the course and activate it as follows. 

```
conda env create -f env-dsci-571.yaml
conda activate 571
```
In order to use this environment in `Jupyter`, you will have to install `nb_conda_kernels` in the environment where you have installed `Jupyter` (typically the `base` environment). You will then be able to select this new environment in `Jupyter`. 

Note that this is not a complete list of the packages we'll be using in the course and there might be a few packages you will be installing using `conda install` later in the course. But this is a good enough list to get you started. 


## Reference Material

#### Books
* [A Course in Machine Learning (CIML)](http://ciml.info/) by Hal Daumé III (also relevant for DSCI 572, 573, 575, 563)
* Introduction to Machine Learning with Python: A Guide for Data Scientists by Andreas C. Mueller and Sarah Guido.
* [The Elements of Statistical Learning (ESL)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
* [Data Mining: Practical Machine Learning Tools and Techniques (PMLTT)](https://www.wi.hs-wismar.de/~cleve/vorl/projects/dm/ss13/HierarClustern/Literatur/WittenFrank-DM-3rd.pdf)
* Artificial intelligence: A Modern Approach by Russell, Stuart and Peter Norvig.
* [Artificial Intelligence 2E: Foundations of Computational Agents](https://artint.info/2e/html/ArtInt2e.htm) (2017) by David Poole and Alan Mackworth (of UBC!).

#### Online courses

* [Mike's CPSC 330](https://github.com/UBC-CS/cpsc330)<br>
Mike is currently teaching an undergrad course on applied machine learning. Unlike DSCI 571, CPSC 330 is a semester-long course but there is a lot of overlap and sharing of notes between these courses. You might find the course  useful.  
* [Mike's CPSC 340](https://ubc-cs.github.io/cpsc340/)
* [Machine Learning](https://www.coursera.org/learn/machine-learning) (Andrew Ng's famous Coursera course)
* [Foundations of Machine Learning](https://bloomberg.github.io/foml/#home) online course from Bloomberg.
* [Machine Learning Exercises In Python, Part 1](http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/) (translation of Andrew Ng's course to Python, also relevant for DSCI 561, 572, 563)

#### Misc

* [A Visual Introduction to Machine Learning (Part 1)](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
* [A Few Useful Things to Know About Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) (an article by Pedro Domingos)
* [Metacademy](https://metacademy.org/) (sort of like a concept map for machine learning, with suggested resources)
* [Machine Learning
  101](https://docs.google.com/presentation/d/1kSuQyW5DTnkVaZEjGYCkfOxvzCqGEFzWBy4e9Uedd9k/present?slide=id.g168a3288f7_0_58)
  (slides by Jason Mayes, engineer at Google)

## Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).
