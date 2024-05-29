import sys
from xray.components.data_ingestion import Data_ingestion
from xray.entity.artifact_entity import data_ingestion_artifact
from xray.entity.config_entity import data_ingestion_config
from xray.exception import Xray_Exception
from xray.logger import logging

class Train_pipeline:
    def __init__(self):
        self.data_ingestion_config=data_ingestion_config()

    def start_data_ingestion(self)->data_ingestion_artifact:
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


if __name__ == "__main__":
    train_pipeline = Train_pipeline()
    train_pipeline.start_data_ingestion()