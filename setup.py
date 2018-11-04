from setuptools import setup, find_packages
from texsite import __version__

# Installation dependencies
install_requires = [
    'django-bootstrap-ui>=0.5,<0.6',
    'wagtail>=2.3,<2.4',
    'wagtailmenus>=2.10,<2.11',
]

# Testing dependencies
testing_extras = [
    'coverage>=4.0.3',
    'flake8>=2.4.1',
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
        'Framework :: Django :: 1.11',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
