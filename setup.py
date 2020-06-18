from setuptools import setup, find_packages
from codecs import open
import numpy
import os
from Cython.Build import cythonize

# thanks Pipy for handling markdown now
ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, 'README.md'), encoding="utf-8") as f:
    README = f.read()

# We can actually import a restricted version of pyecon that
# does not need the compiled code
import pyecon

VERSION = pyecon.__version__

setup(
    name="pyecon",
    description="Dynamic Heterogeneous Agents Equilibrium Models",
    long_description=README,
    long_description_content_type='text/markdown',
    include_dirs=[numpy.get_include()],
    packages=find_packages(),
    data_files=[("", ["LICENSE"])],
    install_requires=['numpy', 'scipy'],
    version=VERSION,
    url="http://pyecon.readthedocs.io/",
    author="Fan Wang",
    author_email="fanwangecon@gmail.com"
)
