#twine upload --repository-url https://test.pypi.org/legacy/ dist/*
from setuptools import setup

setup(
    name='gti',
    version='0.1',
    description='A simple script that shows a Golf GTI when you accidentally type gti instead of git.',
    author='Wouter van der Velde',
    author_email='woutervandervelde2000@hotmail.com',
    url='https://github.com/WoutervdVelde',
    license='MIT',
    scripts=['gti.py'],
    python_requires='>=3.1'   
)