#python setup.py check

#python setup.py sdist

#python setup.py bdist_wheel

#twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from setuptools import setup

setup(
    name='GolfGTI',
    version='1.0.1',
    description='A simple script that shows a Golf GTI when you accidentally type gti instead of git.',
    readme = 'README.md',
    author='Wouter van der Velde',
    author_email='woutervandervelde2000@hotmail.com',
    url='https://github.com/WoutervdVelde',
    license='MIT',
    python_requires='>=3.1',
    entry_points = {
        'console_scripts': ['gti=gti:main'],
    },
)