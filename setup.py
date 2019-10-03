import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-serializer",
    version="1.0.2",
    author="Ximi Hoque",
    author_email="hoque.ximi@gmail.com",
    description="A Python Object-JSON-Object serializer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ximihoque/python-serializer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)