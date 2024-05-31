import os
import sys
from xray.exception import Xray_Exception

class s3_operations:
    def sync_folder_to_s3(self,folder:str, bucket_name:str, bucket_folder_name:str)->None:
        try:
            # Correct the path format by removing extra slashes
            command = f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"
            print(f"Executing command: {command}")  # Debugging print statement
            os.system(command)

        except Exception as e:
            raise Xray_Exception(e, sys)
        
    def sync_folder_from_s3(self,folder:str, bucket_name:str, bucket_folder_name:str)->None:
        try:
            # Correct the path format by removing extra slashes
            command = f"aws s3 sync s3://{bucket_name}/{bucket_folder_name} {folder}"
            print(f"Executing command: {command}")  # Debugging print statement
            os.system(command)
            
        except Exception as e:
            raise Xray_Exception(e, sys)
        
