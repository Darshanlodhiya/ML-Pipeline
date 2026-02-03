from setuptools import find_packages, setup # IT WILL HELP TO SEE/FIND ALL THE TOOLS/PACKAGES USED TO CREATE THIS PROJECT/APP.
from typing import List

# DEFINE 'get_requirements'
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path : str)->List[str]:
    '''
    This function wil return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
        return requirements

# METADATA INFORMATION OF THE ENTIRE PROJECT
setup(
    name = 'ML-Pipeline',
    version = '0.0.1',
    Author = 'Darshan',
    Author_email = 'darshanlodhiya2004@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)