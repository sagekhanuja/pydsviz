from setuptools import setup

setup(
   name='pydsviz',
   version='0.01',
   description='A useful module to visualize data structures',
   author='Sage K',
   packages=['pydsviz'],  #same as name
   install_requires=['collections', 'sys'], #external packages as dependencies
)