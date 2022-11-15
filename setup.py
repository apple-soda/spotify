"""Setup python package configuration."""

from setuptools import setup

setup(
    name="spotify",
    version="0.1.0",
    packages=['spotify'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'requests',
    ],
    python_requires='>=3.10',
)