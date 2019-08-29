from setuptools import setup, find_packages

setup(version='0.0.1',
      name='htast',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
          'translate = htast.cmd.ast2json:main'
          ]
          }
)
