# Getting Started
---
	
You will learn how to:

	- Download and install Anaconda
	- Install Jupyter Notebook
	- Install Rstudio

> "Anaconda is the fastest and easiest way to do Python and R data science and machine learning on Linux, Windows, and Mac OS X. It's the industry standard for developing, testing, and training on a single machine." Through Anaconda you can write in the language Python and/or R. You can use your choice of editors like Jupyter Notebook or RStudio. In this tutoral, you will download *Anaconda* program manager, the langauges *Python*, *R* and the editors *Jupyter Notebook* and *RStudio*. Note: Python will be downloaded by default with Anaconda and R will be downloaded by default with RStudio. These downloads may take a while.

### Downloading and Installing Anaconda
* Download Anaconda [here](https://www.anaconda.com/download/#macos). Choose the latest Python version. (This might take up to 10 minutes or more to download.)
* Once downloaded, double click the downloaded file to launch the installer.
* Installing the Anaconda wizard is pretty straight forward. Just click through all the options without changing anything. ![install Anaconda img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Python-Installation-Wizard.png)
* Then open the Anaconda Navigation program ![Anaconda GUI img](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Anaconda-Navigator-GUI-1024x635.png)

#### Installing Jupyter Notebook
* Jupyter Notebook is an open-source web application that allows you to create and share documents that contain code (not only Python!), visualizations and explainatory text. It allows you to run code sequentially in small sections called cells so you can see what the code is doing.
* Once in Anaconda, click the **Launch** button under Jupyter Notebook. If **Install** appears instead of **Launch**, click **Install** first.
* Once you click **Launch**, a file navigator will open in your browser ![file navigator img](https://github.com/josiahcoad/Intro-Neural-Networks/blob/master/docs/screenshot.png?raw=true)

#### Using Jupyter Notebook
* Open any .ipynb file from the solution folder by clicking on the file in the notebook file navigator.
* Place your curser in the **the first** cell in the jupyter notebook
* Press shift+enter to run the cell
* If successful, the curser should move to the next cell.
* If an asterisk persists to the left of the cell, that cell is currently running. 

#### How to install Python packages needed for building a neural network

**1. Method one: using the conda prompt**

* Open the Anaconda Prompt by Typing "Anaconda Prompt" into your operating system search bar. Alternatively, you can click **New** in the top right corner of the navigator and Choose **Python 3**.
* Type each of the following lines one-by-one into the Anaconda Prompt, pressing enter after each line. (If prompted with "Continue ([y]/n)" type y and press enter.)
  * conda install theano
  * conda install keras
  * conda install tensorflow
  * conda install matplotlib
  * conda install pandas
  * conda install scipy
  * conda install dask

**2. Method two: Through the Anaconda Navigator**

On the left side bar, select enviroments. In the search box **Search Packages**, type the package name and switch from **Installed** to **Not Installed** in the dropdown. Finish by clicking **Apply** in the bottom right corner.

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
