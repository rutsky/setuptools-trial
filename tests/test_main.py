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

    project_src = str(TESTS_DIR / "dummy_project")
    out = virtualenv.run(
        "python setup.py trial",
        capture=True,
        cd=project_src)


def test_test_alias(virtualenv):
    """Test specifying alias for test = trial -m ..."""

    install_setuptools_trial(virtualenv)

    project_src = str(TESTS_DIR / "alias_project")
    out = virtualenv.run(
        "python setup.py test",
        capture=True,
        cd=project_src)
