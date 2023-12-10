from setuptools import setup, find_packages
from pathlib import Path

# Get the directory where this script is located
this_directory = Path(__file__).resolve().parent

# Use an absolute path to the README.rst file
readme_path = this_directory / "README.rst"

# Check if the README file exists
if readme_path.is_file():
    # Read the contents of the README file
    long_description = readme_path.read_text()
else:
    # Provide a placeholder message if the README file is not found
    long_description = "No README.rst file found."

setup(
    # ... other setup parameters ...

    # Set the long_description using the contents of README.rst
    long_description=long_description,
    # Specify the content type for the long_description
    long_description_content_type="text/x-rst",
)
