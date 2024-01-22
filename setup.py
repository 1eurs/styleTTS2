from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='styleTTS2jspeech',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)