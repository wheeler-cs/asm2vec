from setuptools import setup, find_packages

setup(
    name="asm2vec",
    version="1.0",
    description="An unofficial implementation of asm2vec as a standalone Python package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wheeler-cs/asm2vec",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
