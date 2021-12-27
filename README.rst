===================
Learn ML with Spark
===================


.. image:: https://img.shields.io/pypi/v/learn_ml_with_spark.svg
        :target: https://pypi.python.org/pypi/learn_ml_with_spark

.. image:: https://img.shields.io/travis/amjadraza/learn_ml_with_spark.svg
        :target: https://travis-ci.com/amjadraza/learn_ml_with_spark

.. image:: https://readthedocs.org/projects/learn-ml-with-spark/badge/?version=latest
        :target: https://learn-ml-with-spark.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


A project to collect learning resources for Machine Learning with Spark. In this project, we collected the running
Jupyter notebooks compatible to run on Google Colab Environment. All the notebooks are compiled to form a book for
better usage.


* Free software: Apache Software License 2.0
* Documentation: https://learn-ml-with-spark.readthedocs.io.

Project Environment
-------------------

We create the project environment using below command.

``conda env create -f environment.yml -p ./venv``

Update the existing conda environment

``conda env update -f environment.yml -p ./venv``

Activate the environment

``conda activate ./venv``

Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container.

Build the docker container

``docker  build -t ml_spark .``

Run the docker container using docker-compose

``docker-compose up``

Create Docs
------------
The documentation using Sphnix is already set it up.

Use below command to build from `.docs/` location

``make html``

The documents are being created using the notebooks.

TODO
----
* Complete the remaining sections
* Writing Guide to run notebooks using Docker
* Proof Reading.
* Host Docs/tutorials
* Collect the test Data



Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
