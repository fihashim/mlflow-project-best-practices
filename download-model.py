import mlflow
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("databricks")

client = MlflowClient()
my_model = client.download_artifacts("a7106d297ed4438fa37fe111efa50b7e", path="model")
print(f"Placed model in: {my_model}")



