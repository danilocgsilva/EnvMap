from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="env_map",
    version=VERSION,
    description="Common tasks for paths and features in an web environment",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="dev production development web environment",
    url="https://github.com/danilocgsilva/EnvMap",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["env_map"],
    include_package_data=True
)

