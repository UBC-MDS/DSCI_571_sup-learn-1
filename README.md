# DSCI 571: Supervised Learning I

Introduction to supervised machine learning, with a focus on classification. Decision trees, SVM, Naive Bayes, and basic machine learning concepts such as generalization error and overfitting.

## Teaching Team

| Position | Name  | Slack Handle | GHE Handle |
| :------: | :---: | :----------: | :--------: |
| Lecture Instructor | Mike Gelbart | `@mgelbart` | `@mgelbart` |
| Lab Instructor | Varada Kolhatkar | `@Varada` | `@kvarada` |
| Teaching Assistant (L01) | Jasmine Ju | `@Jasmine Ju` | `@xmengju` |
| Teaching assistant (L02) | Joseph Khoury  | `@joseph` | `@josephjk` |
| Teaching Assistant (L03) | Clement Fung | `@Clement Fung` | `@cfung1` |


## Schedule

**Course structure**: this course will be delivered as a [flipped classroom](https://en.wikipedia.org/wiki/Flipped_classroom), which means you are expected to watch the lecture videos _before_ class. While you're not expected to understand everything just from watching a video once, you're expected to come to class with a basic familiarity of what it's all about; we won't be starting again from scratch in class. During the lecture time itself, we will work on practical examples in Python. As a result of the extra 1-2 hours of time spent watching the videos per week, we will aim to make the labs shorter than in other courses.

**Some context**: these videos are from Mike's undergraduate machine learning course, CPSC 340, which contains a lot of the same material. They were filmed in January-April 2018. You can find the accompanying slides, and some supplementary readings, [here](https://ubc-cs.github.io/cpsc340/). By the end of MDS we will cover roughly everything in CPSC 340, although often skipping over the implementation details. On the other hand, we cover machine learning topics that do not appear in CPSC 340, like time series data and natural language data. In MDS we also benefit greatly from the statistical perspective of "stat stream" courses. Finally, we do a little bit on how to implement ML algorithms from scratch in DSCI 572.

**Video timings**: video links have start times embedded in them, which is where you are supposed to start watching from. End times are specified below if you're not supposed to watch the whole video. I recommend watching the videos at 1.25x speed.


| #     | Date       |    Topic       |  To watch _before_ class |
|-------|------------|----------------|---------------------------|
|   1   | 2018-11-14 | [Intro to supervised learning, decision trees](lectures/lecture1.ipynb) |  [Decision tree video](https://youtu.be/WYDPYIe3RpQ?t=199); "Decision Stump: Rule Search (Attempt 3)" at times 31:40-36:35 is optional. |
|   2   | 2018-11-19 | [Fundamentals of learning, cross-validation](lectures/lecture2.ipynb) | [Fundamentals of learning video](https://youtu.be/dPm-KTrJlFU?t=183) and the [part of the KNN video](https://youtu.be/JRF6oELLn0M?t=1248) **up to 29:00** on cross-validation. |
|   3   | 2018-11-21 | [KNN, loess, feature preprocessing](lectures/lecture3.ipynb)     | [The rest of the KNN video](https://youtu.be/JRF6oELLn0M?t=1781) + first part of [naive Bayes video](https://youtu.be/sUtPiyMnkIU?t=195) **up to 16:20**. |
|   4   | 2018-11-26 | [Naive Bayes, evaluation metrics](lectures/lecture4.ipynb)  | [The rest of the Naive Bayes video](https://youtu.be/sUtPiyMnkIU?t=988), first part of [ensemble methods video](https://youtu.be/3SD6fgNGZSo) **up to 14:40**. |
|   5   | 2018-11-28 | Continuing with Lecture 4       | [Understanding ROC/AUC](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)  |
|   6   | 2018-12-03 | [Ensemble methods, random forests](lectures/lecture6.ipynb)  | [The rest of the ensemble methods video](https://youtu.be/3SD6fgNGZSo?t=1386), first part of [clustering video](https://www.youtube.com/watch?v=psDGGjjkhU8&feature=youtu.be&t=109) **up to 8:30**. |
|   7   | 2018-12-05 | [Linear classifiers](lectures/lecture7.ipynb) | [Part of the linear classifier prediction video](https://youtu.be/GMEDGjpJycA?t=436), first part of [linear classifier training video](https://youtu.be/yw2AJZ491S0) **up to 7:00**. <br>Note: the part in the first video about the Perceptron Algorithm is optional, though it's somewhat relevant to DSCI 572 and also has historical significance.<br>Note: unlike the previous videos, here there is a jump from the previous lecture (ensembles, CPSC 340 lecture 7) to this one (linear classifiers, CPSC 340 lecture 18), which may cause a bit of chaos. You will hear words like "regularization" that you may not understand (coming in DSCI 573); when this happens, don't panic. |
|   8   | 2018-12-10 | [Kernels, DSCI 571 review, Blocks 4-6 roadmap, outliers](lectures/lecture8.ipynb)    | _This lecture is optional; you will not be tested on content from it._ |

## Lab Assignments

| #    | Lectures covered   | Due date |
|-----|-------------|----------|
| 1 | 1 | 2018-11-17 18:00
| 2 | 2 & 3 | 2018-11-24 18:00
| 3 | 4 & 5 | 2018-12-01 18:00
| 4 | 6 & 7 | 2018-12-07 18:00


## Reference Material

#### Books

* Artificial intelligence: A Modern Approach by Russell, Stuart and Peter Norvig. 
* Artificial Intelligence 2E: Foundations of Computational Agents (2017) by David Poole and Alan Mackworth (of UBC!). Freely available online at https://artint.info/2e/html/ArtInt2e.html.
* Introduction to Machine Learning with Python: A Guide for Data Scientists by Andreas C. Mueller and Sarah Guido. 
* [A Course in Machine Learning](http://ciml.info/) by Hal Daumé III (also relevant for DSCI 572, 573, 575, 563)

#### Online courses

* [Machine Learning](https://www.coursera.org/learn/machine-learning) (Andrew Ng's famous Coursera course)
* [Foundations of Machine Learning](https://bloomberg.github.io/foml/#home) online course from Bloomberg.
* [Machine Learning Exercises In Python, Part 1](http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/) (translation of Andrew Ng's course to Python, also relevant for DSCI 561, 572, 563)

#### Short posts/articles

* [A Visual Introduction to Machine Learning (Part 1)](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
* [Machine Learning | What’s Inside the Box?](https://medium.com/@randylaosat/machine-learning-whats-inside-the-box-861f5c7e72a3)

#### Misc

* [Metacademy](https://metacademy.org/) (sort of like a concept map for machine learning, with suggested resources)
* [Machine Learning 101](https://docs.google.com/presentation/d/1kSuQyW5DTnkVaZEjGYCkfOxvzCqGEFzWBy4e9Uedd9k/present?slide=id.g168a3288f7_0_58) (slides by Jason Mayes, engineer at Google)
