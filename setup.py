import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swimlane-python-logger",
    version="1.0.5",
    author="Jeremy m Crews",
    author_email="jeremy.m.crews@gmail.com",
    description="Logger wrapper class for Swimlane Integrations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremymcrews/swimlane_python_logger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)