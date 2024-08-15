from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME ="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started  <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed  <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME ="Prepare Base Model"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started  <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed  <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME ="Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started  <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed  <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME ="Evaluation"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started  <<<<<<")
    evaluation = EvaluationPipeline()
    evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed  <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

