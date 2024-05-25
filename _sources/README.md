# ![](lectures/img/571_banner.png)

Welcome to DSCI 571: Supervised Learning I! This course introduces fundamental concepts and techniques in supervised machine learning such as data splitting, cross-validation, generalization, overfitting, the fundamental trade-off, the golden rule, and data preprocessing. Additionally, we will explore popular machine learning algorithms, including decision trees, $k$-nearest neighbors, SVMs, naive Bayes, and linear models, using [the scikit-learn framework](https://scikit-learn.org/stable/).

## Important links 

- [Course Jupyter book](https://pages.github.ubc.ca/mds-2023-24/DSCI_571_sup-learn-1_students/README.html)
- [Course GitHub page](https://github.ubc.ca/MDS-2023-24/DSCI_571_sup-learn-1_students)
- [Slack Channel](https://ubc-mds.slack.com/messages/571_sup-learn-1)
- [Canvas](https://canvas.ubc.ca/courses/123600)
- [Gradescope](https://www.gradescope.ca/courses/11554)
- [iClicker Cloud](https://join.iclicker.com/DAZZ)
- [Reflection Google document](https://docs.google.com/document/d/109zUOV_j3Q12rnKFWWg7JXeCmqXKoWVtioSvEGyDuVw/edit?usp=sharing)
- [YouTube videos](https://www.youtube.com/playlist?list=PLHofvQE1VlGtZoAULxcHb7lOsMved0CuM)
- [Class + office hours calendar](https://ubc-mds.github.io/calendar/)

## Course learning outcomes    

<details>
  <summary>Click to expand!</summary>

By the end of this course, you will be able to:

- Describe supervised learning and its suitability for various tasks.
- Explain key machine learning concepts such as classification, regression, overfitting, and the trade-off in model complexity.
- Identify appropriate data preprocessing techniques for specific scenarios, provide reasons for their selection, and integrate them into machine learning pipelines.
- Develop an intuitive understanding of common machine learning algorithms.
- Build end-to-end supervised machine learning pipelines using Python and scikit-learn on real-world datasets.

</details>

## Deliverables

<details>
  <summary>Click to expand!</summary>
    
The following deliverables will determine your course grade:

| Assessment       | Weight  | Where to submit|
| :---:            | :---:   |:---:  | 
| Lab Assignment 1 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 2 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 3 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 4 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| iClicker participation     | 2%      | [iClicker Cloud](https://join.iclicker.com/DAZZ) | 
| Quiz 1           | 25%     | [Canvas](https://canvas.ubc.ca/courses/123600)     |
| Quiz 2           | 25%     | [Canvas](https://canvas.ubc.ca/courses/123600)     |

See [Calendar](https://ubc-mds.github.io/calendar/) for the due dates. 
</details>

## Teaching Team
<details>
  <summary>Click to expand!</summary>

    
| Role           | Name             | 
| ---------------- | -------------- |
| Lecture Instructor | Varada Kolhatkar |
| Lab Instructor     | Varada Kolhatkar |
| Teaching Assistant | Armin Saadat Boroujeni |
| Teaching Assistant | Daniel Ramandi |
| Teaching Assistant | Faeze Keshavarz  |
| Teaching Assistant | Md Shahriar Rahim Siddiqui|
| Teaching Assistant | Negar Sadrzadeh|
| Teaching Assistant | Prajeet Bajpai |
    
</details>
   
## Lectures 

### Format
<details>
  <summary>Click to expand!</summary>

This course follows a semi-flipped classroom format, where you will watch pre-recorded videos before class. In-class sessions will focus on demos, iClicker questions, Q&A, discussions, and worksheets. It's optional but highly recommended to download the appropriate datasets provided below and put them under your local `lectures/data` directory, and run the lecture Jupyter notebooks on your own and experiment with the code. 

</details>

### Lecture schedule

This course occurs during **Block 2** in the 2023/24 school year.


| Lecture  | Topic  | Assigned videos | Resources and optional readings |
|-------|------------|-----------|-----------|
|      | [Course information](lectures/00_course-information.ipynb) |  📹 Pre-watch: [1.0](https://youtu.be/-1hTcS5ZE4w) | |
|   1   | [Terminology, baselines, decision trees](lectures/01_terminology-baselines-decision-trees.ipynb) | 📹 Pre-watch: [2.1](https://youtu.be/YNT8n4cXu4A), [2.2](https://youtu.be/6eT5cLL-2Vc), [2.3](https://youtu.be/Hcf19Ij35rA), [2.4](https://youtu.be/KEtsfXn4w2E) | |
|   2   | [ML fundamentals](lectures/02_ml-fundamentals.ipynb) | 📹 Pre-watch: [3.1](https://youtu.be/iS2hsRRlc2M), [3.2](https://youtu.be/h2AEobwcUQw), [3.3](https://youtu.be/4cv8VYonepA), [3.4](https://youtu.be/Ihay8yE5KTI) | [An article by Pedro Domingos](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) |
|   3   | [$k$-NNs, SVM RBF]() | 📹 Pre-watch: [4.1](https://youtu.be/hCa3EXEUmQk), [4.2](https://youtu.be/bENDqXKJLmg), [4.3](https://youtu.be/IRGbqi5S9gQ), [4.4](https://youtu.be/ic_zqOhi020), [5.1](https://youtu.be/xx9HlmzORRk) | | 
|   4   | [Preprocessing, pipelines, column transformer]() |  📹 Pre-watch: [5.2](https://youtu.be/G2IXbVzKlt8), [5.3](https://youtu.be/nWTce7WJSd4), [5.4](https://youtu.be/2mJ9rAhMMl0), [6.1](https://youtu.be/to2mukSyvLk) | |
|   5   | [More preprocessing, text features]() | 📹 Pre-watch: [6.2](https://youtu.be/hteVvLwrWZ4) |
|   6   | [Hyperparameter optimization, optimization bias]() |  📹 Pre-watch: [8.1](https://youtu.be/lMWdHZSZMk8), [8.2](https://youtu.be/Z9a9XZ0vQv0) |
|   7   | [Naive Bayes]() | None | <li>[Conditional probability visualization](https://setosa.io/ev/conditional-probability/)</li><li>[Naive Bayes chapter, Jurafsky and Martin](https://web.stanford.edu/~jurafsky/slp3/4.pdf)</li> |
|   8   | [Logistic Regression, multi-class classification]() | 📹 Pre-watch: [7.1](https://youtu.be/HXd1U2q4VFA), [7.2](https://youtu.be/56L5z_t22qE), [7.3](https://youtu.be/_OAK5KiGLg0) | |

### Datasets
Here is the list of [Kaggle](https://www.kaggle.com/) datasets we'll use in this class. 
- [SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)
- [Indian Liver Patient Records](https://www.kaggle.com/uciml/indian-liver-patient-records)
- [IMDB movie reviews](https://www.kaggle.com/utathya/imdb-review-dataset)
- [House Sales in King County](https://www.kaggle.com/harlfoxem/housesalesprediction)
- [The adult census dataset](https://www.kaggle.com/uciml/adult-census-income#)
- [Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)
- [California Housing](https://www.kaggle.com/harrywang/housing?select=housing.csv)

If you want to be extra prepared, you may want to download these datasets in advance and save them under the `lectures/data` directory in your local copy of the repository. 

## Labs 
During labs, you will be given time to work on your own or in groups. There will be a lot of opportunity for discussion and getting help during lab sessions. (Usually I enjoy labs a lot. It's also an opportunity for me to know you a bit better 🙂.) 


## Installation
 
We are providing you with a `conda` environment file which is available [here](env-dsci-571.yaml). You can download this file and create a conda environment for the course and activate it as follows. 

```
conda env create -f env-dsci-571.yaml
conda activate 571
```

In order to use this environment in `Jupyter`, you will have to install `nb_conda_kernels` in the environment where you have installed `Jupyter` (typically the `base` environment). You will then be able to select this new environment in `Jupyter`. If you're unable to see the environment in Jupyter, you might have to install the kernel manually. See the documentation [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html). For more details on this, refer to your [521 lecture 7](https://pages.github.ubc.ca/MDS-2023-24/DSCI_521_platforms-dsci_students/lectures/7-virtual-environments.html#).

I've only attempted to install this environment file on a few machines, and you may encounter issues with certain packages from the `yaml` file when executing the commands above. This is not uncommon and may suggest that the specified package version is not yet available for your operating system via `conda`. When this occurs, you have a couple of options:

1. Modify the local version of the `yaml` file to remove the line containing that package.
2. Create the environment without that package. 
3. Activate the environment and install the package manually either with `conda install` or `pip install` in the environment.   

_Note that this is not a complete list of the packages we'll be using in the course and there might be a few packages you will be installing using `conda install` later in the course. But this is a good enough list to get you started._ 

## Course communication
<details>
  <summary>Click to expand!</summary>

We are all here to support your learning and success in the course and the program. Here's how our communication will work during the course.

### Clarifications on the lecture notes or lab questions

If there is any clarification on the lecture material or lab questions, I'll open an issue in the [course repository](https://github.ubc.ca/MDS-2023-24/DSCI_571_sup-learn-1_students) and tag you. I will also post a Slack message and tag you. **It is your responsibility to read the messages whenever you are tagged.** (I know that there are too many things for you to keep track of. You do not have to read all the messages but please make sure to carefully read the messages whenever you are tagged.) 

### Questions on lecture material or labs

If you have questions about the lecture material or lab questions please post them on the course Slack channel rather than direct messaging me or the TAs. Here are the advantages of doing so: 
- You'll get a quicker response. 
- Your classmates will benefit from the discussion. 

When you ask your question on the course channel, please avoid tagging the instructor unless it's specific for the instructor (e.g., if you notice some mistake in the lecture notes). If you tag a specific person, other teaching team members or your colleagues are discouraged to respond. This decreases the response rate on the channel. 

Please use some consistent convention when you ask questions on Slack to facilitate easy search for others or future you. For example, if you want to ask a question on Exercise 3.2 from Lab 1, start your post with the label `lab1-ex2.3`. Or if you have a question on lecture 2 material, start your post with the label `lecture2`. Once the question is answered/solved, you can add "(solved)" tag before the label (e.g., (solved) `lab1-ex2.3`. Do not delete your post even if you figure out the answer on your own. The question and the discussion can still be beneficial to others.  

### Questions related to grading

If you have concerns related to grading:

1. First, ensure that you have thoroughly reviewed your response, our solution key, and any TA feedback.
2. Verify that your concerns align with our 'Reasonable grading concerns' policy, which you can read [here](https://ubc-mds.github.io/policies/).

If you believe your concerns are valid:
- For assignments: Submit a regrade request on Gradescope.
- For quizzes: Directly message the TA responsible for grading that question. (I will inform you on Slack who has graded what after grades are returned.)
- If you cannot resolve the issue with the TA, send a Slack message to the instructor, including the relevant TA in the conversation.

### Questions related to your personal situation or talking about sensitive information
 
I am open to having a conversation with you. If you'd like to discuss any sensitive matters, please send me a direct message on Slack (and mention/tag me) instead of posting it in the course channel. It may take some time for me to respond, but I'll make every effort to reply as promptly as I can. If I cannot address your issue directly, I can at least direct you to the appropriate person who may be able to assist you. 
</details>

## Reference Material
<details>
  <summary>Click to expand!</summary>
    
### Books
* [A Course in Machine Learning (CIML)](http://ciml.info/) by Hal Daumé III (also relevant for DSCI 572, 573, 575, 563)
* Introduction to Machine Learning with Python: A Guide for Data Scientists by Andreas C. Mueller and Sarah Guido.
* [An Introduction to Statistical
Learning](https://hastie.su.domains/ISLR2/ISLRv2_website.pdf)
* [The Elements of Statistical Learning (ESL)](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
* [Data Mining: Practical Machine Learning Tools and Techniques (PMLTT)](https://www.wi.hs-wismar.de/~cleve/vorl/projects/dm/ss13/HierarClustern/Literatur/WittenFrank-DM-3rd.pdf)
* Artificial intelligence: A Modern Approach by Russell, Stuart and Peter Norvig.
* [Artificial Intelligence 2E: Foundations of Computational Agents](https://artint.info/2e/html/ArtInt2e.htm) (2017) by David Poole and Alan Mackworth (of UBC!).

### Online courses

* [CPSC 330](https://github.com/UBC-CS/cpsc330)<br>
I'm currently teaching an undergrad course on applied machine learning. Unlike DSCI 571, CPSC 330 is a semester-long course but there is a lot of overlap and sharing of notes between these courses.
* [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/ml-intro)
* [Mike's CPSC 340](https://ubc-cs.github.io/cpsc340/)
* [Machine Learning](https://www.coursera.org/learn/machine-learning) (Andrew Ng's famous Coursera course)
* [Foundations of Machine Learning](https://bloomberg.github.io/foml/#home) online course from Bloomberg.
* [Machine Learning Exercises In Python, Part 1](http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/) (translation of Andrew Ng's course to Python, also relevant for DSCI 561, 572, 563)

### Misc

* [A Visual Introduction to Machine Learning (Part 1)](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
* [A Few Useful Things to Know About Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) (an article by Pedro Domingos)
* [Metacademy](https://metacademy.org/) (sort of like a concept map for machine learning, with suggested resources)
* [Machine Learning
  101](https://docs.google.com/presentation/d/1kSuQyW5DTnkVaZEjGYCkfOxvzCqGEFzWBy4e9Uedd9k/present?slide=id.g168a3288f7_0_58)
  (slides by Jason Mayes, engineer at Google)
    
</details>     

## Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).

Enjoy your learning journey in DSCI 571: Supervised Learning I!