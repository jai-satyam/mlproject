from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ='-e .'

def get_requirement(file_path: str)-> List[str]:
    '''
    This function returns the required packages
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace('/n', "") for req in requirement]
    if HYPHEN_E_DOT in requirement:
        requirement.remove(HYPHEN_E_DOT)

    return requirement

setup(
name= 'mlproject',
version='0.0.1',
author='Jai Satyam',
author_email='jsthakur1308@gmail.com',
packages=find_packages(),
##requires=['pandas','numpy','seaborn']
install_requires = get_requirement('requirements.txt')
) 