from setuptools import setup

setup(
    name='bootstrap_2to3',
    version='0.1.1',
    author='Jayesh',
    author_email='jayesh@jayeshv.info',
    entry_points={
        'console_scripts': ['bootstrap_2to3=bootstrap_2to3.bootstrap_2to3:main'],
    },
    packages=['bootstrap_2to3'],
    url='https://github.com/jayeshv/bootstrap_2to3',
    license='BSD licence',
    description='Script to migrate bootstrap 2 templates to bootstrap3.',
    #long_description=open('README.md').read(),
)
