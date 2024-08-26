from setuptools import find_packages, setup

setup(
  name="mcqgenerator",
  version="0.0.1",
  author="tj",
  install_requires=["openai", "langchain", "streamlit", "python-env", "PyPDF2"],
  packages=find_packages()
)