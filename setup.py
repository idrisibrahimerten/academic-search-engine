# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding="utf-8") as f:
    text = f.read()

setup(
      name="academic_search_engine",
      version="1.4",
      author="İdris İbrahim ERTEN",
      author_email="idrisibrahimerten@gmail.com",
      packages=find_packages(),
      long_description=text,
      long_description_content_type='text/markdown',
      )