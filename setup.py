from setuptools import setup, find_packages

with open('requirements/dev.txt') as req:
    requirements = req.read().splitlines()[1:]

setup(
    name='burddy',
    version='0.1-dev',
    packages=find_packages(),
    include_package_data=True,
    url='www.burddy.com',
    author='Alex Frazer',
    author_email='AlexADFrazer@gmail.com',
    description='burddy web application',
    entry_points={'console_scripts': ['burddy = burddy.manage:cli.main']},
    install_requires=requirements
)
