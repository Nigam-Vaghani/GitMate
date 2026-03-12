from setuptools import setup, find_packages

setup(
    name="gitmate",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rich",
        "InquirerPy"
    ],
    entry_points={
        "console_scripts": [
            "hey=gitmate.cli:main"
        ]
    }
)