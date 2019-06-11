from setuptools import setup

setup(name='spintax',
      version='1.0.4',
      description='A Python module for parsing spintax',
      long_description=('A Python module for parsing spintax, unlike any other module this works with nested spintax '
                        'and also allows the user to escape the special characters used in its syntax.'),
      keywords=['spintax', 'spin syntax', 'spintax parser', 'spinning', 'spin'],
      url='http://github.com/AceLewis/spintax',
      download_url='https://github.com/AceLewis/spintax/archive/master.zip',
      author='AceLewis',
      license='GPLv3',
      packages=['spintax'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
          'Topic :: Text Processing',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          ],
      zip_safe=False)
