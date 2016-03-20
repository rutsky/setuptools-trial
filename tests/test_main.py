import os
import pathlib

TESTS_DIR = pathlib.Path(__file__).parent.resolve()
SETUPTOOLS_TRIAL_SRC = TESTS_DIR.parent


def install_setuptools_trial(virtualenv):
    """Install this version of setuptools_trial

    Otherwise tests will load setuptools_trial from PyPI.
    """

    virtualenv.run("pip install {0}".format(SETUPTOOLS_TRIAL_SRC))


def test_virtualenv(virtualenv):
    install_setuptools_trial(virtualenv)

    dummy_project_src = str(TESTS_DIR / "dummy_project")
    virtualenv.run("python setup.py trial",
                   capture=True, cd=dummy_project_src)
