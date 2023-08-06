from kedro.framework.hooks import hook_impl
from .hooks import mlflow_hook
import mlflow

# Set the MLflow tracking URI (use your server URI if using a tracking server)
mlflow.set_tracking_uri("http://127.0.0.1:5000")

class MLflowHook:
    @hook_impl
    def after_node_run(self, node, inputs, outputs):
        # Log parameters and metrics to MLflow
        with mlflow.start_run():
            mlflow.log_params(node.parameters)
            mlflow.log_metrics(node.metrics)

# ...
mlflow_hook = MLflowHook()


hooks = [mlflow_hook]

