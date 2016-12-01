from setuptools import setup

setup(name='spintax',
      version='1.0',
      description='A python module for parsing spintax',
      long_description='A python module for parsing spintax, it can deal with nested spintax and allows the special characters to be escaped',
      url='http://github.com/AceLewis/spintax',
      download_url='https://github.com/AceLewis/spintax/archive/master.zip',
      author='AceLewis',
      license='GPLv3',
      packages=['spintax'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          ],
      zip_safe=False)
