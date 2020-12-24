from setuptools import setup 

with open('README.md', 'r') as f:
    read = f.read()

setup(
    name="better_numbers",
    description="Different base Numbers with useful methods",
    version="0.0.0",
    long_description=read,
    long_description_content_type='text/markdown'
)