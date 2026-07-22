cat > setup.py << 'EOF'
from setuptools import setup, find_packages

setup(
    name='mc-lang',
    version='1.0.0',
    description='The shortest and most secure query language',
    author='rostichar1-hue',
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
    python_requires='>=3.6',
)
EOF
