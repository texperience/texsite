import os
from setuptools import setup, find_packages
from texsite import __version__

# Hard linking doesn't work inside VirtualBox shared folders. This means that you can't use tox in a directory that is
# being shared with Vagrant, since tox relies on `python setup.py sdist` which uses hard links. As a workaround, disable
# hard-linking if setup.py is a descendant of /vagrant. See
# https://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted for more details.
if 'vagrant' in os.path.abspath(__file__).split(os.path.sep):
    del os.link

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='texsite',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description='texsite is a modern web content management system. It is written in Python and built on Wagtail CMS, '
                'which is backed by the Django web framework.',
    long_description=README,
    url='https://github.com/texperience/texsite',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=[
        'django-bootstrap-ui>=0.1,<0.2',
        'wagtail>=1.2,<1.3',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
