from setuptools import setup
from os import path

version = '0.0.1'

repo_base_dir = path.abspath(path.dirname(__file__))

# Long description
readme = path.join(repo_base_dir, 'README.md')
with open(readme) as f:
    long_description = f.read()

setup(
    name='pandoc-inplace-include',
    version=version,
    description='Pandoc filter to allow file inplace includes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='zhijie-yang',
    author_email='zhijie.yang@canonical.com',
    license='MIT',
    url='https://github.com/zhijie-yang/pandoc-inplace-include',

    install_requires=['pandocfilters'],
    # Add to lib so that it can be included
    packages=["pandoc_inplace_include"],
    entry_points={
        'console_scripts': [
            'pandoc-inplace-include = pandoc_inplace_include.main:main'
        ]
    },

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License'
    ]
)
