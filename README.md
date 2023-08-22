## Phishing Attack Domain Detection with Machine Learning

#### 🔥 Official Website 👉 [phishr.vercel.app](https://phishr.vercel.app/)
Enter any URL and our Machine Learning model will scan the URL and tell you if its malicious or not.
<br/>

<div align="center">
<img src="/Imgs/phishr-demo3.gif" width="90%"/>
</div>

## 🎯 Objective
Phishing is a type of fraud in which an attacker impersonates a reputable company or person in order to get sensitive information such as login credentials or account information via email or other communication channels.Phishing is popular among attackers because it is easier to persuade someone to click a malicious link that appears to be authentic than it is to break through a computer's protection measures.


The main goal of this project is  to create a domain authentication system that would detect if a given domain url is legit or fake website created to perform fraud. Multiple ML models will be tested for this problem. A web Interface along with suitable Rest-API's will be created for commercial use.

<div align="center">
<img src="/Imgs/phising_architecture.jpg" width="75%"/>
</div>

## Project Workflow
The project will follow the same approach as used in all ML project. We'll go through different stages of data collection,feature extraction,training and finally deployment of trained model.

- Data Collection
- Feature Extraction
- Model training & evaluation
- Deployment


## Data Collection

For this project we'll need bunch of legitimate and phishing url's,each categorised by (0) and (1). We'll use [this](https://www.kaggle.com/siddharthkumar25/malicious-and-benign-urls) dataset.

It contains 450k domain url's out of which 345k are legitimate and 104k are malicious. The Imbalanced dataset is oversampled using the SOMTE technique,which increases the total number of samples to around 600k.


## Feature Extraction

The dataset till now consist of only legit and malicious urls,in this stage we extract some useful features from these urls and further improve our dataset to make it more suitable for training ML models.

The below mentioned category of features are extracted from the URL data :
- Length based Features ( 5 features extracted)
- Count based Features ( 11 features extracted)
- Binary Features  ( 2 features extracted)


 All together 18 features are extracted from each url of the dataset.


#### (For Further information about the features see the ['Phishing Websites Features.docx'](https://archive.ics.uci.edu/ml/machine-learning-databases/00327/) .

## Model Training

The problem that we are trying to solve is a classification problem,more specifically a 'binary' classification problem. Classification problem comes under supervised machine learning. After feature extraction we'll train multiple ML models using our data and choose the model which gives us best accuracy.

The machine learning models considered to train the dataset in this project are :
- Decision Tree
- Random Forest
- Multilayer Perceptron

(For this dataset MLP gave the highest accuracy (99%) with suitably balanced precision and recall,the trained model is saved [here](https://github.com/deepeshdm/Phishing-Attack-Domain-Detection/tree/main/models))


## 👨‍💻 To run (locally)
1. Import this repository using git command
```
git clone https://github.com/deepeshdm/Phishing-Attack-Domain-Detection.git
```
2. Install all the required dependencies inside a virtual environment
```
pip install -r requirements.txt
```
3. After this just import the get_prediction() from API.py and pass the required arguments to make the prediction.Below is an example,copy the below code snippet and pass the required variable values
```python
from API import get_prediction

# path to trained model
model_path = r"/models/Malicious_URL_Prediction.h5"

# input url
url = "www.tesla.com/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)
```


## 🔥 Web Interface & API Documentation

In order to make it easy for anyone to interact with the model,we created a clean web interface using ReactJS and deployed it on Heroku cloud space. We also created a microservice Rest API, so that developers can use this model in their applications.

- Checkout Official Website : [phishr.vercel.com](https://phishr.vercel.app/)
- Frontend Repository : [here](https://github.com/deepeshdm/phishr) (Newly Updated 2023)
- Backend API repository : [here](https://github.com/deepeshdm/Phishr-API) (Newly Updated 2023)

<div align="center">
<img src="/Imgs/phishr-demo3.gif" width="90%"/>
</div>

## Improvements to make
This project was done just for the sake of learning end-to-end ML deployment,so far less focus was given on optimizing model performances.Further things which can be done for Improving this model :
- Collecting more data which has less "sparse" features.
- Reducing the number of features through feature-selection
- Optimising the model for precion rather than recall.

### Related
- https://github.com/ANG13T/url_genie



