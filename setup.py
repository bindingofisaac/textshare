from setuptools import setup

setup(name='textshare',
      version='0.1',
      description='share your text files easily',
      url='http://github.com/bindingofisaac',
      author='Vivek',
      author_email='bindingofisaacs@gmail.com',
      license='MIT',
      packages=['textshare'],
      entry_points={
          'console_scripts': ['textshare=textshare.command_line:main'],
      },
      zip_safe=False)
