from setuptools import setup, find_packages
from texsite import __version__

# Installation dependencies
install_requires = [
    'django-bootstrap-ui>=0.2,<0.3',
    'wagtail>=1.4,<1.5',
]

setup(
    name='texsite',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description='texsite is a modern web content management system. It is written in Python and built on Wagtail CMS, '
                'which is backed by the Django web framework.',
    long_description=open('README.rst').read(),
    url='https://github.com/texperience/texsite',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
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
