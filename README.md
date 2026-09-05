
# **Health Prediction App**



* This app is for analyze your biometric and lifestyle information and predict your health status.



### **Table of Content**

* ##### [About ](#about)
* ##### [Tech Stack](#tech_stack)
* ##### [Architecture](#architecture)
* ##### [Getting Started](#getting_started)
* ##### [Contribution Guidelines](#contribution_guidelines)
* ##### [Author](#author)



#### **About :**



The app provide to user a well organized and secure form to add their biometric and lifestyle information and by that the model can predict whether they are healthy or not. The user can easily add his information for unlimited times and analyze their health status.





#### **Tech Stack:**



**Programming Language:**

* &#x20;Python 

**Libraries / Tools:**

* pandas/ numpy: to raed and modify the data.
* Streamlit: used to implement a user friendly GUI 
* Sci-Kit learn: used for importing the models and algorithms

&#x20;               - linear\_model, neighbors, svm, tree, ensemble: for selecting the model

&#x20;               - model\_selection: for GridSearchCV

&#x20;               - preprocessing: for encoding

&#x20;               - decomposition: for PCA

&#x20;               - metrices: for the calculation that used to evaluate the model accuracy 

&#x20;                 (f1 score, classification report, confusion matrix)

* imblearn: for importing SMOTE-Tomek algorithm
* seaborn and matplotlib: to visualize the important relations





#### **Architecture:**



Frontend:

&#x20;- Streamlit library 

Backend:

&#x20;- The model pipeline which take the user input and apply the preprocessing steps then

&#x20;   predict the health status

&#x20;                          



#### **Getting Started:**



If you want to use the app you can easily use the app link:https://healthprediction-xfnmehcqkoaznx9czg6rjh.streamlit.app/ ,

or you can install the files and run it locally in your machine by this command: **streamlit run app.py**



to see the detailed steps and all trials go to the colab notebook:https://colab.research.google.com/drive/1oroDx55ljsXA9jb0PkLgp-oYFZw4Po7b?usp=sharing . 

1\. Install the data to can run the cells and this the link of the dataset:https://www.kaggle.com/datasets/mahdimashayekhi/disease-risk-from-daily-habits . 

2\. Install all libraries i have listed in the (Tech Stack) to can run the cell.

3\. After that you can copy the notebook to your drive or download it so, you can easily edit, run and see your changes.



#### **Contribution Guidelines:**



I will be happy if you want to contribute to add some features in my app



&#x20; 1. first fork the repository  to create your own copy of the repository

&#x20; 2. clone your fork

&#x20; 3. create a feature Branch to keep your changes organized

&#x20; 4. set up the environment (go to Getting Started)



#### **Author:**



**If you want any help you can contact me:**

&#x20;**E-mail:** ayayasser282007@gmail.com

&#x20;**LinkedIn:** https://www.linkedin.com/in/aya-yasser-148489339?utm\_source=share\&utm\_campaign=share\_via\&utm\_content=profile\&utm\_medium=android\_app

