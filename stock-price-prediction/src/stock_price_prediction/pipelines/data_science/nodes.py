"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.5
"""

# utilities
from typing import List, Dict
import pandas as pd
import numpy as np
import logging

# sklearn
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



def split_data(df: pd.DataFrame, parameters: Dict) -> List:
    '''
    Splits data into training and test set.
    
     Args:
        data: Source processed data.
        parameters: Parameters defined in parameter.yml.
    
     Returns:
        A list containing split data.
        
    '''
    y = df['Close'].values
    X = df.drop('Close', axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, 
                                                        random_state=42)
    return [X_train, X_test, y_train, y_test]


def train_model(X_train: np.ndarray, y_train: np.ndarray, parameters: Dict) -> xgb:
    '''
    Train the Linear SVC model.
    
     Args:
        X_train_vec: Vectorized training text data.
        y_train: Training data for SDG labels.
        parameters: Parameters defined in parameter.yml.
        
     Returns:
        Trained model.
    '''
    xgbr = xgb.XGBRegressor(verbosity=0)
    regressor = GridSearchCV(xgbr, param_grid=parameters, scoring='neg_mean_squared_error', cv=5)
    regressor.fit(X_train, y_train)

    return regressor

def evaluate_model(reg_model, X_test: np.ndarray, y_test: np.ndarray)-> Dict[str, float]:
    '''
    Generate and log classification report for test data.
    
     Args:
        X_test: Vectorized test text data.
        y_test: Test data for SDG.
        classifier: Trained model.
        
    '''
    y_pred = reg_model.predict(X_test)
    #y_proba = sdg_classifier.predict_proba(X_test_vec)
    #best_n = np.argsort(y_proba, axis=1)[:,-1:]
    #best_1 = np.argmax(y_proba, axis=1)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    score = r2_score(y_test, y_pred)
    #score = f1_score(y_test, y_pred, average='weighted')
    logger = logging.getLogger(__name__)
    logger.info("Model has an rmse %.3f on test data.", rmse)
    logger.info("Model has an r2_score %.3f on test data.", score)
    logger.info("Model has an mae %.3f on test data.", mae)

    return {"r2_score": score,"rmse": rmse, "mae": mae}


''' ================================== 

     ML predictions of new data

 ==================================== '''

#will add this node when Database is ready
#once we make predictions, we need to store these preds somewhere,
#so that they can be shown on streamlit
# we need to discuss, lets first keep a back log of data and predict it and show 
# on streamlit instead of having live updates and predictions
# we should output a col with top 3 labels and their probabilites


def remove_col(new_data: pd.DataFrame) -> List:
    new =new_data.drop('Close', axis=1)
    return new

def get_predictions(reg_model, new_data: pd.DataFrame, new: np.ndarray) -> List:
    # Assuming the "target_column" is not present in the new_data DataFrame
    # You may need to preprocess the new_data DataFrame to match the format used during training
    print(type(reg_model))

    # Make predictions on the new_data
    #X=new_data.drop('Close', axis=1)
    #dnew = xgb.DMatrix(new)
    predictions = reg_model.predict(new)

    # Add the predictions as a new column to the new_data DataFrame
    new_data["predicted_target"] = predictions
    print(new_data.head(6))

    return new_data

     

