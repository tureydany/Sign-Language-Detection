import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

projectName="signLanguage"

list_of_files=[
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",
    f"{projectName}/__init__.py",
    f"{projectName}/components/data_ingestion.py",
    f"{projectName}/components/data_validation.py",
    f"{projectName}/components/model_trainer.py",
    f"{projectName}/components/model_pusher.py",
    f"{projectName}/configuration/__init__.py",
    f"{projectName}/configuration/s3_operations.py",
    f"{projectName}/constant/__init__.py",
    f"{projectName}/constant/training_pipeline/__init__.py",
    f"{projectName}/constant/application.py",
    f"{projectName}/entity/__init__.py",
    f"{projectName}/entity/artifacts_entity.py",
    f"{projectName}/entity/config_entity.py",
    f"{projectName}/exception/__init__.py",
    f"{projectName}/logger/__init__.py",
    f"{projectName}/pipeline/__init__.py",
    f"{projectName}/pipeline/training_pipeline.py",
    f"{projectName}/utils/__init__.py",
    f"{projectName}/utils/main_utils.py",
    "template.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path()

    file_dir,file_name=os.path.split(filepath)

    if file_dir!=" ":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory {file_dir} for {file_name}")

    if (not os.path.exists(file_name) or os.path.getsize()==0):
        with open(filepath,"r") as f:
            pass
        logging.info(f"Creating empty file : {file_name}")

    else:
        logging.info(f"{file_name} is already created")
            
    

