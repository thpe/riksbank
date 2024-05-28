""" setup.py """
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riksbank",
    version="1.0.0",
    author="Thomas Petig",
    author_email="thomas@petig.eu",
    description="Access the API of the Swedish central bank (riksbanken)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thpe/riksbank",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'pandas'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
