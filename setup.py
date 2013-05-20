from distutils.core import setup

setup(name='django-random-blocks',
      version='0.1.0',
      description='Django Random Blocks',
      author='Nathaniel Tucker',
      author_email='me@ntucker.me',
      url='https://github.com/ntucker/django-random-blocks',
      py_modules=['randomblocks'],
      packages=['django-random-blocks'],
      install_requires=['django>=1.4', 'django-jsonfield>=0.9.4', ],
      )
