import re
from os.path import join, dirname
import setuptools


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        regex = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = regex.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(join(dirname(__file__), fname), "r") as fh:
        return fh.read()


setuptools.setup(
    name="sqlalchemy-easy-profile",
    version=find_version("easy_profile/__init__.py"),
    author="Dmitri Vasilishin",
    author_email="vasilishin.d.o@gmail.com",
    description="An easy profiler for SQLAlchemy queries",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/kandziu/sqlalchemy-easy-profile",
    packages=setuptools.find_packages(exclude=('test*',)),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["sqlalchemy", "easy", "profile", "profiler", "profiling"],
    tests_require=["coverage", "mock", "sqlalchemy"]
)