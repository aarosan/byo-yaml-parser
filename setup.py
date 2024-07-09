from setuptools import setup, find_packages

setup(
    name='byo_yaml_parser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'yaml_parser=yaml_parser.main:main',
        ],
    },
)