from setuptools import find_packages, setup

version = '0.0.1a'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Cryptobento',
    version=version,
    author='Alex Deng',
    description='An info aggregator webapp for learning about cryptocurrencies and blockchain technology.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)