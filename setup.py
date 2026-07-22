from setuptools import setup, find_packages

setup(
    name='mc-lang',
    version='1.0.0',
    description='The shortest and most secure query language',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='rostichar1-hue',
    author_email='',
    url='https://github.com/rostichar1-hue/MicroCode',
    packages=find_packages(),
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'micro=microcode.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
