from setuptools import find_packages, setup
from typing import List

#defining constant '-e .' that connects requirements.txt to setup.py
HYPEN_E_DOT='-e .'

#creating func to extract it from requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requiremnets
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements] #to remove '\n' recorded while reading lines  replacing it with list comprehention

        if HYPEN_E_DOT in requirements: #.remove() to remove HYPEN_E_DOT 
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
name='machinelearningproject1',
version='0.0.1',
author='harshal',
author_email='datadrivenharshal@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)
