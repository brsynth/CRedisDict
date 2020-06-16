import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ComplexRedisDict",
    version="0.0.7",
    author="Joan Hérisson",
    author_email="joan.herisson@univ-evry.fr",
    description="Dictionnary with complex data stored in a Redis database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brsynth/RedisDict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
