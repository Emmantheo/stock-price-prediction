"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from stock_price_prediction.pipelines.data_preprocessing.nodes import feature_engineering


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        [node(
            func=feature_engineering,
            inputs="train_data",
            outputs="cleaned_train_data",
            name="train_preprocess_data_node"
        ),
        node(
            func=feature_engineering,
            inputs="new_data",
            outputs="cleaned_new_data",
            name="test_preprocess_data_node"
        )
        ]
    )
    data_preprocessing = pipeline(
        pipe=pipeline_instance,
        inputs=["train_data", "new_data"],
        namespace = "data_preprocessing",
        outputs = ["cleaned_train_data", "cleaned_new_data"]
    )
    return data_preprocessing