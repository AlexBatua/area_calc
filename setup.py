from setuptools import setup, find_packages

setup(
    name='area_test_for_word',
    version='0.1',
    packages=find_packages(),
    url='http://example.com',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple library for calculating areas of shapes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    test_suite='tests',
)