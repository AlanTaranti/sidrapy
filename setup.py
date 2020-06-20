# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sidrapy.sdk import VERSION

description = 'sidrapy'

with open("README.md") as f:
    long_description = f.read()

maintainer = 'Alan Taranti'
maintainer_email = 'alan.taranti@gmail.com'

oldest_supported_python_3_version = '3.5'

setup(
    name='sidrapy',
    version=VERSION,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    packages=find_packages(),
    license='MIT',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlanTaranti/Sidrapy',
    keywords='ibge, sidra, api, brasil, brazil, estatistica, statistics',
    include_package_data=True,
    zip_safe=False,
    python_requires=">={}".format(oldest_supported_python_3_version),
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
