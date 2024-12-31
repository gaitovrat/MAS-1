import os
from pathlib import Path

from setuptools import find_packages, setup

FILE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


setup(
    name="mas",
    version="0.1",
    description="A Python package for mas functionality",
    long_description=(FILE_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
