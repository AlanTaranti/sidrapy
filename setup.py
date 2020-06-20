# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sidrapy.sdk import VERSION

description = 'sidrapy'

with open("README.md") as f:
    long_description = f.read()

autor = 'Alan Taranti'
autor_email = 'alan.taranti@gmail.com'

setup(
    name='sidrapy',
    version=VERSION,
    author=autor,
    author_email=autor_email,
    packages=find_packages(),
    license='MIT',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlanTaranti/Sidrapy',
    keywords='ibge, sidra, api',
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests', 'pandas'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ]
)
