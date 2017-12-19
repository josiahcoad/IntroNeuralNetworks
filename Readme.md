# Learn Deep Learning from the Basics
![Oxford Course Banner](https://scontent-lht6-1.xx.fbcdn.net/v/t31.0-8/23550047_1857784714249682_818662786257132584_o.jpg?oh=58428ed99e30824d180088dc46de3615&oe=5AA37404 "Banner")

### Course Objectives
- Learn what deep learning is, and how it relates to simple statistical models.
- Become comfortable with many commonly heard words of machine learning at a high level (more concept, less math)
  - forward propogation
  - activation functions
  - loss functions
  - learning rate
  - backwards propagation and gradient decent
  - epochs and batches
- Start using some of the tools for Neural Network programming (numpy, pandas, keras)
- Build a predictive (regression and classification) ML model using keras and interpret the output
- **Final: Classify digits with the MNIST data set**

Please note the programming instructions and slides for each lesson are explained in person and thus not fully documented online.  

Please also note that the course structure has been gleaned from other superb online courses (ie *Deep Learning in Python* from datacamp.com) and thus may look familiar if you've taken other online classes.  
### Repository Structure
* ./Practicals
  * fill-in-the-blanks in the code to deepen your understanding of the code behind the concepts.
* ./Solutions
  * Stuck with one of the coding practicals? Check out the solutions for each practical where all the blanks are filled in.  
* ./Quizes
  * Test your knowledge with these interactive questionairs. See immediately how you compare to others who have answered the questions.  

### Setup for Chapters 1-2

* Download this git repository.   
  * click the green button "Clone or Download" in top right hand corner of this page  ![Green Button Img](https://s31.postimg.org/r45t0i9a3/imageedit_9_4620369683.jpg)
  * click "Download Zip"  
  * Open the file's location on your computer and unzip the folder
  * Move folder to a place where you can find it easily

##### Download and Install Anaconda
* Download Anaconda [here](https://www.anaconda.com/download/#macos). Choose the Python 3.6 version. (This might take up to 10 minutes to download)
* Once downloaded, double click the .exe file to launch the installer.
* Installing the Anaconda wizard is pretty straight forward. Just click through all the options without changing anything. ![install Anaconda img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Python-Installation-Wizard.png)
* Then open the Anaconda Navigation program ![Anaconda GUI img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Navigator-GUI-1024x635.png)

##### Setting up Jupyter Notebook
* Jupyter Notebook is an open-source web application that allows you to create and share documents that contain code, visualizations and explainatory text. It allows you to run code sequentially in small sections called cells so you can see what the code is doing.
* Once in Anaconda, click the "Launch" button under Jupyter Notebook
* It will open a file navigator in your browser ![file navigator img](https://github.com/josiahcoad/Intro-Neural-Networks/blob/master/TutorialPics/Screen%20Shot%202017-12-18%20at%2010.39.21%20PM.png?raw=true)

* Now navigate to where you put the Intro-Neural-Networks-master folder, the unziped version of the file you downloaded at the beginning
![Neural Networks folder img](https://github.com/josiahcoad/Intro-Neural-Networks/blob/master/TutorialPics/Screen%20Shot%202017-12-18%20at%2010.40.01%20PM.png?raw=true)

##### Using Jupyter Notebook
* Open any file from the Solution folder by clicking on it (suggest starting in chapter1_solution.ipynb)
* Place your curser in the **the first** cell in the jupyter notebook
* Press shift+enter to run the cell
* If successful, the curser should move to the next cell.
* Continue in this fashion through all cells, reading each cell and trying to understand it before moving onto the next.

### Setup for Chapter 3-4

##### Install packages needed for building a neural network
* Open the Anaconda Prompt by Typing "Anaconda Prompt" into your operating system search bar
* Type each of the following lines one-by-one into the Anaconda Prompt, pressing enter after each line.
  * conda install sklearn
  * conda install theano
  * conda install keras
  * conda install tensorflow
  * conda install matplotlib
  * conda install pandas
  * conda install scipy
