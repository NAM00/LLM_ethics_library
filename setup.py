from setuptools import setup, find_packages

setup(
    name='LLM_ethics_library',
    version='0.1.0',
    description='A package for evaluating ethical dilemmas with LLMs',
    author='Nazia Afsan Mowmita',
    packages=find_packages(include=["LLM_ethics_library", "LLM_ethics_library.*"]),
    install_requires=[
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
