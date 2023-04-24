from setuptools import find_packages
from setuptools import setup

setup(
    name='sapphire_llm',
    version='0.1.0',
    install_requires=['Your-Library'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license='MIT',
    author_email='agravat@google.com',
    description='Your main project'
)
