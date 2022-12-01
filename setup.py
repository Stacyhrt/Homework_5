from setuptools import setup

setup(
    name='Homework_5',
    version='0.1.0',    
    description='Homework 5 DSSS',
    url='https://github.com/Stacyhrt/Homework_5.git',
    author='Stacy Huerta',
    author_email='stacy.huerta@fau.de',
    license='Apache License 2.0',
    packages=['snowflake'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache License 2.0',  
        'Operating System :: POSIX :: WINDOWS',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9.13',

    ],
)