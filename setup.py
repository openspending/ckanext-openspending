from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(
    name='ckanext-openspending',
    version=version,
    description="Automatically model and submit financial data to the OpenSpending platform",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Tryggvi Bjorgvinsson',
    author_email='tryggvi.bjorgvinsson@okfn.org',
    url='',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openspending'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'ckanext-budgets'
        'requests'
    ],
    entry_points='''
        [ckan.plugins]
        openspending=ckanext.openspending.plugin:OpenSpendingPlugin
    ''',
)
