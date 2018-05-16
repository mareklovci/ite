from setuptools import setup

setup(name='ite',
      version='0.1.0',
      packages=['ite'],
      entry_points={
          'console_scripts': [
              'ite = ite.__main__:main',
              'server = ite.server:main'
          ]
      },
      )
