
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flock-py",
    version="0.1.6",
    author="Meng yangyang",
    author_email="mengyy_linux@163.com",
    description="File lock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hotbaby/flock-py",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
