from setuptools import setup, find_packages

# Read requirements.txt and store its contents in a list
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='styleTTS2',
    version='0.1',
    packages=find_packages(),
     package_data={
        '': ['*.*'], 
    },
    install_requires=required,  
    long_description_content_type='text/markdown',
    url='https://github.com/1eurs/styleTTS2',
)
