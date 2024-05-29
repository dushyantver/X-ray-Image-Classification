import sys

from xray.cloud_storage.s3_operations import s3_operations
from xray.constant.training_pipeline import *
from xray.entity.config_entity import data_ingestion_config
from xray.entity.artifact_entity import data_ingestion_artifact
from xray.exception import Xray_Exception
from xray.logger import logging

class Data_ingestion:
    def __init__(self, data_ingestion_config:data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config

        self.s3 = s3_operations()

    def get_data_from_s3(self):
        try:
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")

            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
            )

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")
        except Exception as e:
            raise Xray_Exception(e, sys)
        
    def initiate_data_ingestion(self)->data_ingestion_artifact:
        logging.info(
            "Entered the initiate_data_ingestion method of Data ingestion class"
        )
        try:
            self.get_data_from_s3()

            Data_ingestion_artifact: data_ingestion_artifact = data_ingestion_artifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path,
            )

            logging.info(
                "Exited the initiate_data_ingestion method of Data ingestion class"
            )

            return Data_ingestion_artifact
        except Exception as e:
            raise Xray_Exception(e, sys)