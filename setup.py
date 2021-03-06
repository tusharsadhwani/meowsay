import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meowsay",
    version="1.0.2",
    author="Tushar Sadhwani",
    author_email="tushar.sadhwani000@gmail.com",
    description="Cowsay, but better.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tusharsadhwani/meowsay",
    py_modules=['meowsay'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['meowsay=meowsay:meowsay'],
    }
)
