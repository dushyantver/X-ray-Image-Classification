import sys

from xray.exception import Xray_Exception
from xray.pipeline.training_pipeline import Train_pipeline


def start_training():
    try:
        train_pipeline = Train_pipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise Xray_Exception(e, sys)


if __name__ == "__main__":
    start_training()