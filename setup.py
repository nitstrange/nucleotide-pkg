import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nucleotide-pkg-hoursdesajib", # Replace with your own username
    version="0.0.3",
    author="Ahasan Habib",
    author_email="sajib.ahasan@gmail.com",
    description="A small example package for test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nitstrange/nucleotide-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)