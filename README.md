## Phishing Attack Domain Detection by Machine Learning

<div align="center">
<img src="/Imgs/phising.gif" width="50%"/>
</div>

## Objective
Phishing is a type of fraud in which an attacker impersonates a reputable company or person in order to get sensitive information such as login credentials or account information via email or other communication channels.Phishing is popular among attackers because it is easier to persuade someone to click a malicious link that appears to be authentic than it is to break through a computer's protection measures.


The main goal of this project is  to create a domain authentication system that would detect if a given domain url is legit or fake website created to perform fraud. Multiple ML models will be tested for this problem. A web Interface along with suitable Rest-API's will be created for commercial use.

<div align="center">
<img src="/Imgs/phising_architecture.jpg" width="65%"/>
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




## Model Training




## Web Interface & API Documentation








