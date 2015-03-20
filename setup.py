from setuptools import setup  # find_packages
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-rest-api',
    version='0.1.1',
    description='Django REST API',
    long_description=long_description,
    url='https://github.com/skies-io/django-rest-api',
    author='Skies',
    author_email='aurelien.maigret@skies.io',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django rest api',
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages=['rest_api'],
    install_requires=['Django>=1.6'],
)
