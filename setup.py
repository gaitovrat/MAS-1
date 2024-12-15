from setuptools import setup, find_packages
import yaml
import os
from pathlib import Path

FILE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


def load_dependencies() -> list[str]:
    out: list[str] = []
    dependencies: list[str]

    with open(FILE_DIR / "environment.yml", "r", encoding="utf-8") as fd:
        config = yaml.safe_load(fd)

    dependencies = config.get("dependencies", [])
    if not dependencies:
        return []

    dependencies = dependencies[1:]  # Skip "python=3.12"
    for dependency in dependencies:
        if isinstance(dependency, dict):
            dependencies.extend(dependency.get("pip", []))
        else:
            out.append(dependency)

    return out


setup(
    name="mas",
    version="0.1",
    description="A Python package for mas functionality",
    long_description=(FILE_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=load_dependencies(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
