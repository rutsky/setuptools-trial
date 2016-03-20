from setuptools import find_packages, setup

setup(
    name="project",
    version="1.0.0",
    setup_requires="setuptools_trial",
    test_suite="project.test",
    tests_require=[
        "Twisted",
    ],
    packages=find_packages(exclude=("tests",)),
)
