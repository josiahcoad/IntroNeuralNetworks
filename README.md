# Practical Neural Networks from the Basics
---

### Course Objectives
- Learn what "deep learning" is, and how it relates to simple statistical models.
- Become comfortable with many commonly heard **words** of machine learning at a high level (*more concept, less math*)
  - forward propogation
  - activation function
  - loss function
  - learning rate
  - gradient decent
  - backwards propagation
  - batches
  - epochs
- Start using some of the tools for Neural Network programming (keras, tensorflow, some helpful packages: (numpy, pandas))
- Build a predictive (regression and classification) ML model using keras and interpret the output

*Please note the programming instructions and slides for each lesson are explained in person and thus not fully documented online.*

### Setup for Chapters 1-2
* Download this git repository.   
  * click the green button "Clone or Download" in top right hand corner of this page  ![Green Button Img](http://www.cs.williams.edu/~dbarowy/cs334s18/assets/tutorials/github/github-clone-button.png)
  * click "Download Zip"
  * Open the file's location on your computer and unzip the folder
  * Move folder to a place where you can find it easily

##### Download and Install Anaconda
* Download Anaconda [here](https://www.anaconda.com/download/#macos). Choose the latest Python version. (This might take up to 10 minutes to download)
* Once downloaded, double click the .exe file to launch the installer.
* Installing the Anaconda wizard is pretty straight forward. Just click through all the options without changing anything. ![install Anaconda img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Python-Installation-Wizard.png)
* Then open the Anaconda Navigation program ![Anaconda GUI img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Navigator-GUI-1024x635.png)
* (for a more indepth tutorial, please see my installation.md in the docs folder)

##### Setting up Jupyter Notebook
* Jupyter Notebook is an open-source web application that allows you to create and share documents that contain code, visualizations and explainatory text. It allows you to run code sequentially in small sections called cells so you can see what the code is doing.
* Once in Anaconda, click the "Launch" button under Jupyter Notebook
* It will open a file navigator in your browser ![file navigator img](https://github.com/josiahcoad/Intro-Neural-Networks/blob/master/TutorialPics/Screen%20Shot%202017-12-18%20at%2010.39.21%20PM.png?raw=true)

* Now navigate to where you put the IntroNeuralNetworks-master folder, (the unziped version of the file you downloaded)
![Neural Networks folder img](https://github.com/josiahcoad/Intro-Neural-Networks/blob/master/TutorialPics/Screen%20Shot%202017-12-18%20at%2010.40.01%20PM.png?raw=true)

##### Using Jupyter Notebook
* Open any file in Jupyter Notebook by clicking on the file in the Jupyter Notebook application
* Place your curser in the **the first** cell in the jupyter notebook
* Press shift+enter (or click the little green play icon) to run the cell (remember a cell is just a section of code)
* If successful, the curser should move to the next cell and a number should show up at the left of the cell.
* If your cell is stuck, you can tell it is still processing by a astric-star showing up to left of the cell instead of a number.
* Continue in this fashion through all cells. Look closely at each cell and try to understand it before moving onto the next.

##### Install packages needed for building a neural network
* Open the Anaconda Prompt by Typing "Anaconda Prompt" into your operating system search bar
* Type each of the following lines one-by-one into the Anaconda Prompt, pressing enter after each line. (If prompted with "Continue ([y]/n)" type y and press enter.)
  * conda install theano
  * conda install keras
  * conda install tensorflow
  * conda install matplotlib
  * conda install pandas
  * conda install scipy
  * conda install dask

### Acknowledgements
Special thanks to ![Deep Learning in Python](https://www.datacamp.com/courses/deep-learning-in-python) course from Datacamp.
and inspiration from the wonderful ![Mastering Machine Learning](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) blog. I highly recomend these for continued learning.
