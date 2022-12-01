from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='0.1.0',    
    description='Homework 5 DSSS',
    url='https://github.com/Stacyhrt/Homework_5.git',
    author='Stacy Huerta',
    author_email='stacy.huerta@fau.de',
    license='Apache License 2.0',
    packages= find_packages(),
    install_requires=['turtles',
                      'numpy',                     
                      ],
  )