import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dutch-pluralizer",
    version="0.0.5",
    description="Generates Dutch plural and singular nouns in a very imperfect way using Hunspell dictionaries. Why imperfect? Because the Dutch language is full of exceptions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/KeesCBakker/dutch-pluralizer-py",
    author="Kees C. Bakker / KeesTalksTech",
    author_email="info@keestalkstech.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dutch_pluralizer"],
    include_package_data=True,
    install_requires=["cython", "cyhunspell"],
    entry_points={
        "console_scripts": [
            "dutch_pluralizer=dutch_pluralizer.__main__:main",
        ]
    },
)
