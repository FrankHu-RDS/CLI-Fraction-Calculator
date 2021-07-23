from setuptools import setup

setup(
    name='process',
    version=1.0,
    packages=['process'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['process = process.cli.main:main']}
)
