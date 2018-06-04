__author__="Dmdv"
__date__ ="$16.01.2012 16:49:12$"

from setuptools import setup, find_packages

setup (
  name = 'Tests',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3', 'scipy'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Dmdv',
  author_email = '',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.
)