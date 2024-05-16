from setuptools import find_packages, setup
from typing import List


Hypen_Dot_E = "-e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    this function is return list of function
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if Hypen_Dot_E in requirements:
            requirements.remove(Hypen_Dot_E)
    return requirements
             


setup(
    name='machine_learning_project',
    version="0.0.1",
    author='Ram',
    author_email='rammahto645@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)