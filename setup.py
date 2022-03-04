import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="JupyterPy",
    version="1.0.0",
    description="Automation API to convert Jupyter Notebook (.ipynb) JSON format into Python file (.py), with the capabilities to add magic functions to determine which cells to be exported.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bengsoon/jupyterpy",
    author="Bengsoon Chuah",
    author_email="bengsoonchuah@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pathlib", "regex", "nbformat"],
)