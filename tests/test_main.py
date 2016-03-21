import sys

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

import pytest

TESTS_DIR = pathlib.Path(__file__).parent.resolve()
SETUPTOOLS_TRIAL_SRC = TESTS_DIR.parent


def install_setuptools_trial(virtualenv):
    """Install this version of setuptools_trial

    Otherwise tests will load setuptools_trial from PyPI.
    """

    virtualenv.run("pip install {0}".format(SETUPTOOLS_TRIAL_SRC))


@pytest.mark.xfail(sys.version_info >= (3,) and sys.platform == 'win32',
                   reason="Twisted tests fails on Windows on Python 3")
def test_basic(virtualenv):
    install_setuptools_trial(virtualenv)

    project_src = str(TESTS_DIR / "dummy_project")

    # Run trial command should succeed.
    out = virtualenv.run(
        "python setup.py trial",
        capture=True,
        cd=project_src)
    assert "PASSED (successes=1)" in out

    # Run trial with custom reporter
    out = virtualenv.run(
        "python setup.py trial --reporter=text",
        capture=True,
        cd=project_src)


@pytest.mark.xfail(sys.version_info >= (3,) and sys.platform == 'win32',
                   reason="Twisted tests fails on Windows on Python 3")
def test_test_alias(virtualenv):
    """Test specifying alias for test = trial"""

    install_setuptools_trial(virtualenv)

    project_src = str(TESTS_DIR / "alias_project")
    out = virtualenv.run(
        "python setup.py test",
        capture=True,
        cd=project_src)
    assert "PASSED (successes=1)" in out
