from setuptools import setup, find_packages

setup(
    name='mc-lang',
    version='1.0.0',
    description='The shortest and most secure query language',
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
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
