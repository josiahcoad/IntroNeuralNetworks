# Getting Started
	
You will learn how to:

	- Download and install Anaconda
	- Install Jupyter Notebook
	- Install Rstudio

> "Anaconda is the fastest and easiest way to do Python and R data science and machine learning on Linux, Windows, and Mac OS X. It's the industry standard for developing, testing, and training on a single machine." Through Anaconda you can write in the language Python and/or R. You can use your choice of editors like Jupyter Notebook or RStudio. In this tutoral, you will download *Anaconda* program manager, the langauges *Python*, *R* and the editors *Jupyter Notebook* and *RStudio*. Note: Python will be downloaded by default with Anaconda and R will be downloaded by default with RStudio. These downloads may take a while.

#### Download the Git Repo
* Download this git repository.   
  * click the green button "Clone or Download" in top right hand corner of this page  ![Green Button Img](http://www.cs.williams.edu/~dbarowy/cs334s18/assets/tutorials/github/github-clone-button.png)
  * click "Download Zip"
  * Open the file's location on your computer and unzip the folder
  * Move folder to a place where you can find it easily

#### Download and Install Anaconda
* Download Anaconda [here](https://www.anaconda.com/download/#macos). Choose the latest Python version. (This might take up to 10 minutes to download)
* Once downloaded, double click the .exe file to launch the installer.
* Installing the Anaconda wizard is pretty straight forward. Just click through all the options without changing anything. ![install Anaconda img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Python-Installation-Wizard.png)
* Then open the Anaconda Navigation program ![Anaconda GUI img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Navigator-GUI-1024x635.png)
* (for a more indepth tutorial, please see my installation.md in the docs folder)

#### Setting up Jupyter Notebook
* Jupyter Notebook is an open-source web application that allows you to create and share documents that contain code, visualizations and explainatory text. It allows you to run code sequentially in small sections called cells so you can see what the code is doing.
* Once in Anaconda, click the "Launch" button under Jupyter Notebook
* It will open a file navigator in your browser

* Now navigate to where you put the IntroNeuralNetworks-master folder, (the unziped version of the file you downloaded)

#### Using Jupyter Notebook
* Open any file in Jupyter Notebook by clicking on the file in the Jupyter Notebook application
* Place your curser in the **the first** cell in the jupyter notebook
* Press shift+enter (or click the little green play icon) to run the cell (remember a cell is just a section of code)
* If successful, the curser should move to the next cell and a number should show up at the left of the cell.
* If your cell is stuck, you can tell it is still processing by a astric-star showing up to left of the cell instead of a number.
* Continue in this fashion through all cells. Look closely at each cell and try to understand it before moving onto the next.

#### How to install Python packages needed for building a neural network

**1. Method one: using the conda prompt**

* Open the Anaconda Prompt by Typing "Anaconda Prompt" into your operating system search bar
* Type each of the following lines one-by-one into the Anaconda Prompt, pressing enter after each line. (If prompted with "Continue ([y]/n)" type y and press enter.)
  * conda install theano
  * conda install keras
  * conda install tensorflow
  * conda install matplotlib
  * conda install pandas
  * conda install scipy
  * conda install dask
  * conda install seaborn
  * conda install sklearn

##### Alternate route for tensorflow installation

If tensorflow install isn't working, try the following:

```python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0-py3-none-any.whl```

**2. Method two: Through the Anaconda Navigator**

On the left side bar, select enviroments. In the search box **Search Packages**, type the package name and switch from **Installed** to **Not Installed** in the dropdown. Finish by clicking **Apply** in the bottom right corner.

**3. Method three: Installing Directly From the Notebook**

If conda install is not working for you to install packages, you can try the following.

Install a pip package in the current Jupyter kernel by putting the following lines in the first cell of your notebook:
```
import sys
!{sys.executable} -m pip install numpy
```
> And replace numpy with all the other packages

### Installing R Studio
* Once in Anaconda, click the **Launch** button under rstudio. If **Install** appears instead of **Launch**, click **Install** first. Installing will take a while.
* Once you click **Launch**, RStudio will open in a new app window.
* Read more about [R Studio](https://www.datacamp.com/community/blog/jupyter-notebook-r)!


#### Using R Studio
- Like jupyter notebook, put your cursor on a line you want to run and press **shift** and **enter**.

#### How to Install R Packages (from within Rstudio)
simple! Just type the following line in the Rstudio workspace with your packagename and run with command above.

```install.packages("packagename")```


#### Installing RKernel for Jupyter Notebooks
- Ok, so Python and R are programming *languages*. RStudio and Jupyter Notebooks are Programming Editors. In analogy, English is a language and Microsoft Word is an editor. So this should lead to the question, "why can't we write R in Jupyter notebook?" ¯\\_(ツ)_/¯ Good question. Turns out we can.
- In fact, once you've installed R Studio, you should have r installed. Open Jupyter notebook and in the right upper corner, click new. In the dropdown should be the option **R**. Clicking it will make a new R document. try typing something simple like **a = 5** into the first cell and running it.
