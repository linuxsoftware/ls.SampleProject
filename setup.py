
#  ls.sampleproject
#  -----------

import codecs
from setuptools import setup, find_packages

setup(name="ls.sampleproject",
      version="0.1.0",
      description="Prints 6x6 Sator Squares",
      long_description=codecs.open("README.rst", encoding="utf-8").read(),
      keywords=["sator", "rotas"],
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules"
                  ],
      platforms="any",
      author="David Moore",
      author_email="dave@linuxsoftware.nz",
      url="https://github.com/linuxsoftware/ls.sampleproject",
      license="MIT",
      install_requires=["inflect"],
      test_requires=["coverage"],
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=["ls"],
      test_suite="ls.sampleproject.tests",
      zip_save=False,
     )
