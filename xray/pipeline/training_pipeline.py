import sys
from xray.components.data_ingestion import Data_ingestion
from xray.components.data_transformation import DataTransformation
from xray.entity.artifact_entity import DataIngestionArtifact
from xray.entity.artifact_entity import DataTransformationArtifact
from xray.entity.config_entity import DataIngestionConfig
from xray.entity.config_entity import DataTransformationConfig
from xray.exception import Xray_Exception
from xray.logger import logging

class Train_pipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_transformation_config=DataTransformationConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:

            logging.info("Getting the data from s3 bucket")

            data_ingestion = Data_ingestion(
                data_ingestion_config=self.data_ingestion_config,
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise Xray_Exception(e, sys)
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        
        logging.info("Entered the start_data_transformation method of TrainPipeline class")

        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )

            logging.info(
                "Exited the start_data_transformation method of TrainPipeline class"
            )

            return data_transformation_artifact

        except Exception as e:
            raise Xray_Exception(e, sys)



    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_transformation_artifact: DataTransformationArtifact = (
                self.start_data_transformation(
                    data_ingestion_artifact=data_ingestion_artifact
                )
            )

            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise Xray_Exception(e, sys)

            