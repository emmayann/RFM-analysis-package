#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas','squarify','matplotlib.pyplot', 'seaborn' ]

test_requirements = ['pytest>=3', ]

setup(
    author="Emma Hovhannisyan",
    author_email='emmahovhannisyan02@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This package ",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='rfmanalysis',
    name='rfmanalysis',
    packages=find_packages(include=['rfmanalysis', 'rfmanalysis.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/emmayann/rfmanalysis',
    version='0.1.0',
    zip_safe=False,
)
