
# coding: utf-8

# # Using SkLearn to Create a Neural Network for Classification

# Execute the following command to load the iris dataset into a Python dataframe:

# In[1]:


import pandas as pd

# Location of dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign column names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=names)


# The above script simply downloads the iris data, assigns the names i.e. 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', and 'Class' to the columns of the dataset, and then loads it into the irisdata dataframe.
# 
# To see what this dataset actually looks like, execute the following command:

# ### Data Exploration
# We always want to visualize and understand our data first!

# In[2]:


irisdata.head()


# In[3]:


import seaborn as sns
g = sns.pairplot(irisdata, hue="Class")


# ### Preprocessing
# You can see that our dataset has five columns. The task is to predict the class (which are the values in the fifth column) that the iris plant belongs to, which is based upon the sepal-length, sepal-width, petal-length and petal-width (the first four columns). The next step is to split our dataset into attributes and labels. Execute the following script to do so:

# In[4]:


# Assign data from first four columns to X variable
X = irisdata.iloc[:, 0:4]

# Assign data from first fifth columns to y variable
y = irisdata.select_dtypes(include=[object])  


# In[5]:


y.head()  


# You can see that the values in the y series are categorical. However, neural networks work better with numerical data. Our next task is to convert these categorical values to numerical values. But first let's see how many unique values we have in our y series. Execute the following script:

# In[6]:


y.Class.unique()  


# We have three unique classes 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'. Let's convert these categorical values to numerical values. To do so we will use Scikit-Learn's LabelEncoder class.
# 
# Execute the following script:

# In[7]:


from sklearn import preprocessing  
le = preprocessing.LabelEncoder()

y = y.apply(le.fit_transform)


# ### Train Test Split
# To avoid over-fitting, we will divide our dataset into training and test splits. The training data will be used to train the neural network and the test data will be used to evaluate the performance of the neural network. This helps with the problem of over-fitting because we're evaluating our neural network on data that it has not seen (i.e. been trained on) before.
# 
# To create training and test splits, execute the following script:

# In[8]:


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20) 


# The above script splits 80% of the dataset into our training set and the other 20% in to test data.
# 
# Feature Scaling
# Before making actual predictions, it is always a good practice to scale the features so that all of them can be uniformly evaluated. Feature scaling is performed only on the training data and not on test data. This is because in real world, data is not scaled and the ultimate purpose of the neural network is to make predictions on real world data. Therefore, we try to keep our test data as real as possible.
# 
# The following script performs feature scaling:

# In[9]:


from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  


# ### Training and Predictions
# And now it's finally time to do what you have been waiting for, train a neural network that can actually make predictions. To do this, execute the following script:

# In[10]:


from sklearn.neural_network import MLPClassifier  
clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)  
clf.fit(X_train, y_train.values.ravel())  


# Yes, with Scikit-Learn, you can create neural network with these three lines of code, which all handles much of the leg work for you. Let's see what is happening in the above script. The first step is to import the MLPClassifier class from the sklearn.neural_network library. In the second line, this class is initialized with two parameters.
# 
# The first parameter, hidden_layer_sizes, is used to set the size of the hidden layers. In our script we will create three layers of 10 nodes each. There is no standard formula for choosing the number of layers and nodes for a neural network and it varies quite a bit depending on the problem at hand. The best way is to try different combinations and see what works best.
# 
# The second parameter to MLPClassifier specifies the number of iterations, or the epochs, that you want your neural network to execute. Remember, one epoch is a combination of one cycle of feed-forward and back propagation phase.
# 
# By default the 'relu' activation function is used with 'adam' cost optimizer. However, you can change these functions using the activation and solver parameters, respectively.
# 
# In the third line the fit function is used to train the algorithm on our training data i.e. X_train and y_train.
# 
# The final step is to make predictions on our test data. To do so, execute the following script:

# In[11]:


predictions = clf.predict(X_test)  


# ### Evaluating the Algorithm
# We created our algorithm and we made some predictions on the test dataset. Now is the time to evaluate how well our algorithm performs. To evaluate an algorithm, the most commonly used metrics are a confusion matrix, precision, recall, and f1 score. The confusion_matrix and classification_report methods of the sklearn.metrics library can help us find these scores. The following script generates evaluation report for our algorithm:

# In[12]:


from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,predictions))


# > Reference: Thanks to [Stack Abuse](https://stackabuse.com/introduction-to-neural-networks-with-scikit-learn/) for the material that I copy/pasted from your website ❤️ 

# In[22]:


cm = confusion_matrix(y_test,predictions)
figure = sns.heatmap(cm / sum(cm), cmap="YlGnBu", annot=True, fmt=".1%")


# [plot_decision_boundaries](https://github.com/NSAryan12/nn-from-scratch/blob/master/nn-from-scratch.ipynb)
