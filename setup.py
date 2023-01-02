#python setup.py check

#python setup.py sdist

#python setup.py bdist_wheel

#twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='GolfGTI',
    version='1.1.1',
    description='A simple script that shows a Golf GTI when you accidentally type gti instead of git.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Wouter van der Velde',
    author_email='woutervandervelde2000@hotmail.com',
    url='https://github.com/WoutervdVelde',
    license='MIT',
    python_requires='>=3.1',
    packages=['gti'],
    entry_points = {
        'console_scripts': ['gti=gti.app:show_gti'],
    },
    include_package_data=True,
)