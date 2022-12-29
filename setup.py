from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name="crusty",
        version="0.0.1",
        author="Seve Martinez",
        author_email="motorific@gmail.com",
        description="calculates a fibonacci number",
        long_description=long_description,
        url="https://github.com/seve-martinez/crusty",
        install_requires=[
            "PyYAML>=4.1.2",
            "dill>=0.2.8"
        ],
        packages=find_packages(exclude=['tests', ]),
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ],

        entry_points={
            'console_scripts': [
                'fib-number = fib_py.cmd.fib_numb:fib_numb'
            ],
        },
        python_requires='>=3',
        tests_require=['pyest'],
        extras_require={
            'server': ["Flask>=1.0.0"]
        }
)


