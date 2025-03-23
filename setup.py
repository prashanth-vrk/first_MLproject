from setuptools import find_packages,setup
## this will automatically find out all the packages that are available
## in the entire machine learning application in the directory the we have created

from typing import List

HYPEN_E_DOT='-e .'

## fun that return libraries needed to install
def get_requirements(file_path:str)->List[str]:
    '''
      this fun will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        ## every line is appended by new line so to remove we use this

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements





## doing setup (essentials of packages)
setup(
name='ml_project',
version='0.0.1',
author='prash',
author_email='vprashanth516@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')## this fun returns all librares in the file
)