from setuptools import setup, find_packages
from texsite import __version__

# Installation dependencies
install_requires = [
    'django>=2.2,<2.3',
    'django-bootstrap-ui>=1.0,<2.0',
    'wagtail>=2.7,<2.8',
    'wagtailmenus>=3.0,<4.0',
]

# Testing dependencies
testing_extras = [
    'coverage>=5.0,<6.0',
    'flake8>=3.7,<4.0',
    'tox>=3.14,<4.0',
]

setup(
    name='texsite',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description=
        'texsite delivers great and ready-to-use page templates for the modern, flexible and user-focused web content'
        'management system Wagtail CMS backed by the popular Django web framework, both written in Python.',
    long_description=open('README.rst').read(),
    url='https://github.com/texperience/texsite',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
