from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f_obj:
        requirements=f_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements

setup(
    name='Dymond-Price-Prediction',
    version='0.0.1',
    author='Bhumil',
    author_email='bhumilc88@gmail.com',
    include_dirs=get_requirements('Requirements.txt'),
    packages=find_packages()
)