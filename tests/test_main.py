import os


TESTS_DIR = os.path.dirname(__file__)
SETUPTOOLS_TRIAL_SRC = os.path.abspath(
    os.path.join(TESTS_DIR, os.path.pardir))


def test_virtualenv(virtualenv):
    dummy_project_src = os.path.abspath(
        os.path.join(TESTS_DIR, "dummy_project"))

    virtualenv.run("pip install {0}".format(SETUPTOOLS_TRIAL_SRC))

    virtualenv.run("python setup.py trial".format(SETUPTOOLS_TRIAL_SRC),
                   capture=True, cd=dummy_project_src)
