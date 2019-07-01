from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
NAME = 'GapBot'
DESCRIPTION = "gapbot is python Gap messenger's api bot library"
URL = 'https://github.com/MrMahdi313/gapbot'
EMAIL = 'm.m.z.m12363@gmail.com'
AUTHOR = 'MrMahdi313'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.0.4'
LICENSE = 'GNU Lesser General Public License v3.0'
try:
    with open(path.join(here, "requirements.txt"), encoding="utf-8") as r:
        REQUIRED = [i.strip() for i in r]
except FileNotFoundError:
    REQUIRED = ['Flask==1.0.3', 'requests==2.22.0',]
try:
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        README = f.read()
except FileNotFoundError:
    README = 'https://github.com/MrMahdi313/GapBot/blob/master/README.md'
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    project_urls={
        "Tracker": "https://github.com/MrMahdi313/gapbot/issues",
        "API Docs Reference": "https://developer.gap.im/doc",
        "Source(Branch master)": "https://github.com/MrMahdi313/gapbot",
        "Source(Branch dev)": "https://github.com/MrMahdi313/gapbot/tree/dev",
        "Documentation": "https://gapbot.readthedocs.io/en/latest",
    },
    keywords='gap bot api',
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    packages=find_packages(include=['gapbot*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Natural Language :: Persian",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
    zip_safe=False
)
