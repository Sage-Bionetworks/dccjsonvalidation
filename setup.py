import os
from setuptools import setup, find_packages

# Get the version number
about = {}
curr_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(curr_dir, "dccjsonvalidation", "__version__.py")) as f:
    exec(f.read(), about)

setup(name="dccjsonvalidation",
      version=about["__version__"],
      description="DCC JSON schema validation and template generation",
      url="https://github.com/Sage-Bionetworks/dccjsonvalidation",
      author="Cindy Molitor",
      author_email="cindy.molitor@sagebase.org",
      license="Apache",
      packages=find_packages(),
      zip_safe=False,
      python_requires=">=3.5",
      install_requires=[
          "pandas>=0.20.0",
          "synapseclient>=1.9",
          "jsonschema[format]>=3.0.2"
      ])
