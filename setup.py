# ----------------------
#  ls.sampleproject
# ----------------------

import os
import io
from pathlib import Path
from setuptools import setup, find_packages


# allow setup.py to be run from any path
here = Path(__file__).resolve().parent
os.chdir(str(here))

with io.open("README.rst", encoding="utf-8") as readme:
    README = readme.read()


setup(name="ls.sampleproject",
      use_scm_version={
          'write_to':  "ls/sampleproject/_version.py",
      },
      description="Prints 6x6 Sator Squares",
      long_description=README,
      keywords=["sator", "rotas"],
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules" ],
      platforms="any",
      author="David Moore",
      author_email="david@linuxsoftware.co.nz",
      url="https://github.com/linuxsoftware/ls.sampleproject",
      license="MIT",
      packages=find_packages(where=".", exclude=["ls.sampleproject.tests"]),
      setup_requires=["setuptools_scm"],
      install_requires=["inflect"],
      tests_require=["coverage"],
      data_files=[
          ('my_data', ['data/data_file']),
      ],
      test_suite="ls.sampleproject.tests",
     )
