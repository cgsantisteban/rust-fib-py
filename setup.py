from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="rust_fib_py",
    version="0.0.1",
    author="Alex",
    author_email="ale@",
    description="Calculates a Fibonacci number",
    long_description="A basic library that \
      calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/cgsantisteban/rust-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fib-number = rust_fib_py.fib_numb:fib_numb',
        ]
    }
)
