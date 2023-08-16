# stock-price-prediction
This project aims to predict stock prices of a single company, Uniqlo listed in the Japanese stock market. One of the largest clothing retailers in Japan, Uniqlo has been around for over five decades. The prediction models are built using historical stock market data ranging from 2012 to 2016 and various machine learning techniques.

## Table of Contents
  1. [Introduction](#introduction)

  2. [Data](#data)
  
  3. [Models](#models)
  4. [Result](#results)
  5. [APP Demo](#app_demo)
  6. [Challenges](#challenges)
  7. [Usage](#usage)
  8. [Contributing](#contributing)
  9. [License](#license)


## Introduction
Stock price prediction plays a crucial role in financial analysis and decision-making. This project focuses specifically on predicting stock prices for Uniqluo in the Japanese market. By leveraging historical data and advanced machine learning techniques, I aim to develop accurate models that can forecast future stock prices.

## Data
The dataset used for this project consists of historical stock market data for Uniqluo listed in the Japanese stock market. It includes attributes such as opening price, closing price, high price, low price, trading volume, and other relevant factors. The data is collected from reliable sources and covers from 2012 to 2016. There is also a test data to validate the performance of the model. 

## Models
We employ various machine learning algorithms to predict stock prices. Some of the models implemented in this project include:

Linear Regression: A basic regression model that establishes a linear relationship between the input features and the target variable.

Random Forest: A powerful ensemble learning method that combines multiple decision trees to generate predictions.

xgboost: XGBoost's combination of boosting, regularization, and efficient optimization techniques makes it a go-to algorithm for many machine learning time series analysis projects and other real-world supervised learning projects due to its strong predictive performance and versatility.

## Result
The following image shows how the predicted price compares to the real price. The image shows the model was able to predict the prices closely to the actual real prices.

<img width="655" alt="result_stock" src="https://github.com/Emmantheo/stock-price-prediction/assets/89465917/6330edc4-185d-4b05-bc17-d3670ec254bd">

## APP Demo
Link to the deployed app: https://stock-price-predict-fsmqhpvkyc4mek2unbflob.streamlit.app/

P.S: The app is still being worked on.
https://github.com/Emmantheo/stock-price-prediction/assets/89465917/1d93b0bf-aae1-4d5a-8c7a-3a98ac6f3f27


## Challenges
1. Limited amount of data to train on which resulted in having a smaller size of test data.
2. Installation of packages such as the fbprophet package. I had to install all the dependencies one after the other. Dependencies such as:
    pystan
   
    holidays
   
    convertdate
   
    lunarcalendar
   
    cmdstanpy


## Usage
To use this project, follow these steps:

Clone the repository: git clone https://github.com/Emmantheo/stock-price-prediction
Check the wiki page for more details.

## Contributing
Contributions to this project are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. You can also open an issue to report any problems or provide feedback.









