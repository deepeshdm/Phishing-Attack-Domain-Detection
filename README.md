## Phishing Attack Domain Detection by Machine Learning

<div align="center">
<img src="/Imgs/phising.gif" width="50%"/>
</div>

## Objective
Phishing is a type of fraud in which an attacker impersonates a reputable company or person in order to get sensitive information such as login credentials or account information via email or other communication channels.Phishing is popular among attackers because it is easier to persuade someone to click a malicious link that appears to be authentic than it is to break through a computer's protection measures.


The main goal of this project is  to create a domain authentication system that would detect if a given domain url is legit or fake website created to perform fraud. Multiple ML models will be tested for this problem. A web Interface along with suitable Rest-API's will be created for commercial use.

<div align="center">
<img src="/Imgs/phising_architecture.jpg" width="75%"/>
</div>

## Project Workflow
The project will follow the same approach as used in all ML project. We'll go through different stages of data collection,feature extraction,training and finally deployment of trained model.

```python
Data Collection --> Feature Extraction --> Training --> Deployment
```


## Data Collection

For this project we'll need bunch of legitimate and phishing url's,each categorised by (0) and (1). 

We'll use this kaggle dataset : https://www.kaggle.com/siddharthkumar25/malicious-and-benign-urls.
It contains 450k domain url's out of which 345k are legitimate & 104k are malicious. From this dataset 10,000 url's are randomly collected from each class to train ML models.

The collected datasets are uploaded in '[Data](https://github.com/deepeshdm/Phishing-Attack-Domain-Detection/tree/main/Data)' directory of this repository.


## Feature Extraction

The dataset till now consist of only legit and malicious urls,in this stage we extract some useful features from these urls and further improve our dataset to make it more suitable for training ML models.

The below mentioned category of features are extracted from the URL data :

- Address Bar based Features ( 9 features extracted)
- Domain based Features ( 4 features extracted)
- HTML & Javascript based Features ( 4 features extracted)

 All together 17 features are extracted from 5000 URLs of each class and the final dataset is stored in '[Phishing_Detection2.csv](https://github.com/deepeshdm/Phishing-Attack-Domain-Detection/blob/main/Data/Phishing_Detection2.csv)' file in the Data folder of this repository.

#### (For Further information about the features see the '[features file](https://github.com/deepeshdm/Phishing-Attack-Domain-Detection/blob/main/Data/Phishing%20Websites%20Features-converted.pdf)' in the data folder)


## Model Training

The problem that we are trying to solve is a classification problem,more specifically a 'binary' classification problem. Classification problem comes under supervised machine learning. After feature extraction we'll train multiple ML models using our data and choose the model which gives us best accuracy.

The machine learning models considered to train the dataset in this project are :
- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- k-nearest neighbors
- GradientBoost
- Multilayer Perceptron



## Web Interface & API Documentation








