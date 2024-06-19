# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tracker',
    version='1.0.0',
    description='LeetCode Rank Tracker',
    long_description=readme,
    author='egg528',
    author_email='rnjsdntjr26@kakao.com',
    url='https://github.com/egg528/leetcode-rank-tracker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

