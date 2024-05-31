from datetime import datetime
from typing import List

import torch

## Data ingestion constant

TIMESTAMP: datetime=datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

ARTIFACT_DIR: str="artifacts"

BUCKET_NAME: str="xrayimage"

S3_DATA_FOLDER: str="data"

### Data Transformation Constant

CLASS_LABEL_1: str="NORMAL"

CLASS_LABEL_2: str="Pneumania"

BRIGHTNESS: int=0.10

CONTRAST: int=0.1

SATURATION: int=0.10

HUE: int=0.1

RESIZE: int=224

CENTERCROP: int=224

RANDOMROTATION: int=10

NORMALIZE_LIST_1: List[int] = [0.485, 0.456, 0.406]

NORMALIZE_LIST_2: List[int] = [0.229, 0.224, 0.225]

TRAIN_TRANSFORMS_KEY: str = "xray_train_transforms"

TEST_TRANSFORM_FILE: str = "test_transform.pkl"

TRAIN_TRANSFORM_FILE: str = "train_transform.pkl"

BATCH_SIZE:int = 2

SHUFFLE: bool = False

PIN_MEMORY: bool = True

#model trainer constants

TRAINED_MODEL_DIR: str = "trained_model"

TRAINED_MODEL_NAME: str = "model.pt"

DEVICE: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

STEP_SIZE: int = 6

GAMMA: int = 0.5

EPOCH: int = 10

BENTOML_MODEL_NAME: str = "xray_model"

BENTOML_SERVICE_NAME: str = "xray_service"

BENTOML_ECR_URI: str = "xray_bento_image"

PREDICTION_LABEL: dict = {"0": CLASS_LABEL_1, 1: CLASS_LABEL_2}