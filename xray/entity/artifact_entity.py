from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader



@dataclass
class data_ingestion_artifact:
    train_file_path:str
    test_file_path:str