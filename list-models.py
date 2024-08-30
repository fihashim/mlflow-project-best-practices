import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("databricks")
# Initialize the MLflow client
client = MlflowClient()

# Search for all registered models
registered_models = client.search_registered_models()

# Print the names of all registered models
print("Registered Models:")
for model in registered_models:
    print(f"- {model.name}")
