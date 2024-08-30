from setuptools import setup, find_packages
import os

def get_data_files():
    data_files = []
    if os.name == 'posix':
        data_files.append(('share/man/man1', ['davodtime.1']))
    return data_files

setup(
    name="davodtime",
    version="0.1.0",
    author="David Blue",
    author_email="davidblue@extratone.com",
    description="A command line tool to display time in various formats.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/extratone/davodtimecli",
    packages=find_packages(),
    install_requires=[
        "pytz",
    ],
    entry_points={
        "console_scripts": [
            "davodtime=davodtime.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
