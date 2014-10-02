from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

description = "Automatically model and submit budgets to the OpenSpending"
with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='ckanext-openspending',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='ckan openspending',
    author='Tryggvi Bjorgvinsson',
    author_email='tryggvi.bjorgvinsson@okfn.org',
    url='https://github.com/tryggvib/ckanext-openspending',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openspending'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'ckanext-budgets',
        'requests'
    ],
    entry_points='''
        [ckan.plugins]
        openspending=ckanext.openspending.plugin:OpenSpendingPlugin
    ''',
)
