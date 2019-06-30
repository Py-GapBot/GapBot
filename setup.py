from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="gapbot",
    version='0.0.3',
    description="gapbot is python Gap messenger's api bot library",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='GNU Lesser General Public License v3.0',
    author='MrMahdi313',
    author_email='m.m.z.m12363@gmail.com',
    url='https://github.com/MrMahdi313/gapbot',
    project_urls={
        "Tracker": "https://github.com/MrMahdi313/gapbot/issues",
        "API Docs Reference": "https://developer.gap.im/doc",
        "Source(Branch master)": "https://github.com/MrMahdi313/gapbot",
        "Source(Branch dev)": "https://github.com/MrMahdi313/gapbot/tree/dev",
        "Documentation": "https://gapbot.readthedocs.io/en/latest",
    },
    keywords='gap bot api',
    python_requires='>=3.6',
    install_requires=requires,
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
