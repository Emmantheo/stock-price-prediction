"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from stock_price_prediction.pipelines.data_science.nodes import split_data, train_model, evaluate_model, remove_col, get_predictions


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(
                func=split_data,
                inputs=["cleaned_train_data", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train", "parameters"],
                outputs="reg_model",
                name="reg_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["reg_model", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
            node(
                func=remove_col,
                inputs='cleaned_new_data',
                outputs='new',
                name="remove_col_node",
            ),
            node(
                func=get_predictions,
                inputs=['reg_model', 'cleaned_new_data','new'],
                outputs='predictions',
                name="predict_new_data_node",
            ),
        ]
    )
    data_science = pipeline(
        pipe=pipeline_instance,
        inputs=["cleaned_train_data","cleaned_new_data"],
        namespace = "data_science",
        outputs = 'predictions'
    )
    return data_science