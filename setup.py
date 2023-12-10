from setuptools import setup, find_packages
from pathlib import Path

# put the contents of your README file into the long_description
this_directory = Path(__file__).parent
readme_path = this_directory / "README.rst"

try:
    long_description = readme_path.read_text()
except FileNotFoundError:
    print(f"File {readme_path} does not exist. Please ensure the file is in the correct location.")
    long_description = ""

setup(
    long_description=long_description
)