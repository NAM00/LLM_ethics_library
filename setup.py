from setuptools import setup, find_packages

setup(
    name="your_package",
    version="0.1.0",
    packages=find_packages(),  # Automatically find packages in folders with __init__.py
    install_requires=[],       # Or load from requirements.txt
    python_requires='>=3.6',
)