from dataclasses import dataclass

# 1.These data classes provide a structured way to store and pass around information and 
# results within machine learning pipeline.
# 2.Each class is designed to encapsulate specific types of information or artifacts

# Data Ingestion Artifact includes information related to data ingestion.
@dataclass
class DataIngestionArtifact:
    trained_file_path: str  # Path to the training data file.
    test_file_path: str     # Path to the test data file.

@dataclass
# Data Validation Artifact includes information about data validation and potential issues.
class DataValidationArtifact:
    validation_status: bool           # Indicates whether data validation was successful or not
    valid_train_file_path: str        # Path to the valid training data file
    valid_test_file_path: str         # Path to the valid test data file
    invalid_train_file_path: str      # Path to the invalid training data file (if any issues found)
    invalid_test_file_path: str       # Path to the invalid test data file (if any issues found)
    drift_report_file_path: str       # Path to a report on data drift

@dataclass
# Data Transformation Artifact includes information related to data transformation.
class DataTransformationArtifact:
    transformed_object_file_path: str  # Path to the transformed data object.
    transformed_train_file_path: str   # Path to the transformed training data file.
    transformed_test_file_path: str    # Path to the transformed test data file.

@dataclass
# Classification Metric Artifact includes classification metrics.
class ClassificationMetricArtifact:
    f1_score: float         # F1-score for the classification model.
    precision_score: float  # Precision score for the classification model.
    recall_score: float     # Recall score for the classification model.

@dataclass
# Model Trainer Artifact includes information related to model training module.
class ModelTrainerArtifact:
    trained_model_file_path: str       # Path to the trained machine learning model file.
    train_metric_artifact: ClassificationMetricArtifact  # Metrics on the training data.
    test_metric_artifact: ClassificationMetricArtifact   # Metrics on the test data.

@dataclass
# Model Evaluation Artifact includes information related to model evaluation.
class ModelEvaluationArtifact:
    is_model_accepted: bool        # Indicates whether the model is accepted.
    improved_accuracy: float       # Improvement in model accuracy.
    best_model_path: str           # Path to the best model.
    trained_model_path: str        # Path to the trained model.
    train_model_metric_artifact: ClassificationMetricArtifact  
    best_model_metric_artifact: ClassificationMetricArtifact   

@dataclass
# Model Pusher Artifact includes information related to pushing/deploying the model.
class ModelPusherArtifact:
    saved_model_path: str     # Path to the saved model fiel.
    model_file_path: str      # Path to the model file.

# These artifacts are used to initialize training pipeline and components


