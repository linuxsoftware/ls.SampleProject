# ----------------------
#  ls.sampleproject
# ----------------------

import os
import io
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with io.open("README.rst", encoding="utf-8") as readme:
    README = readme.read()

# Package dependencies
install_requires = [
    "inflect",
]

# Testing dependencies
testing_extras = [
    # Required for running the tests
    "tox>=2.3.1,<2.4",

    # For coverage and PEP8 linting
    "coverage>=4.1.0,<4.2",
    "flake8>=3.2.0,<3.3",
    "flake8-colors>=0.1.6,<1",
    "isort==4.2.5",

    # For test site
    "django==2.0",
    "wagtail==2.0b1",
]

# Documentation dependencies
documentation_extras = [
]

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
      install_requires=install_requires,
      extras_require={'testing':   testing_extras,
                      'docs':      documentation_extras, },
      tests_require=testing_extras,
      #include_package_data=True,
      #package_data={},
      data_files=[
          ('my_data', ['data/data_file']),
      ],
      # test_suite="ls.sampleproject.tests",
      # zip_safe=False,
     )
