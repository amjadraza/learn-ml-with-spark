#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="MA Raza",
    author_email='amjadraza24@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A project to collect learning resources for Machine Learning with Spark",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='learn_ml_with_spark',
    name='learn_ml_with_spark',
    packages=find_packages(include=['learn_ml_with_spark', 'learn_ml_with_spark.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/amjadraza/learn_ml_with_spark',
    version='0.1.0',
    zip_safe=False,
)
