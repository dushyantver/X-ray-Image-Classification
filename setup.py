from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name="x_ray",
    version="0.0.2",
    author="dushyant",
    author_email="dushyantdchss@gmail.com",
    install_requires=get_requirements(r"D:\\Data_analytics_new\\MLOPS\\X-ray_image_classification\\requirements_dev.txt"),
    packages=find_packages()
)
