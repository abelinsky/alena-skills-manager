import os

from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


def required(requirements_file):
    with open(os.path.join(BASEDIR, requirements_file), "r") as file_handler:
        requirements = file_handler.read().splitlines()
        return [
            pkg
            for pkg in requirements
            if pkg.strip() and not pkg.startswith("#")
        ]


setup(
    name="asm",
    version="0.1.0",
    packages=["asm"],
    install_requires=required("requirements.txt"),
    python_requires=">=3.6",
    author="Alexander Belinsky",
    description="Alena Skills Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={"console_scripts": {"asm=asm.__main__:main"}},
)
