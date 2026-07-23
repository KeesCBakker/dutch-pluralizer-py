import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="dutch-pluralizer",
    version="0.0.39",
    description="Generates Dutch plural and singular nouns in a very imperfect way using Hunspell dictionaries. Why imperfect? Because the Dutch language is full of exceptions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/KeesCBakker/dutch-pluralizer-py",
    author="Kees C. Bakker / KeesTalksTech",
    author_email="info@keestalkstech.com",
    license="MIT",
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["cffi>=1.15.0"],
    entry_points={
        "console_scripts": [
            "dutch_pluralizer=dutch_pluralizer.__main__:main",
        ]
    },
)
