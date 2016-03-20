import os


def test_virtualenv(virtualenv):
    tests_dir = os.path.dirname(__file__)
    setuptools_trial_src = os.path.abspath(
        os.path.join(tests_dir, os.path.pardir))
    dummy_project_src = os.path.abspath(
        os.path.join(tests_dir, "dummy_project"))

    virtualenv.run("pip install {0}".format(setuptools_trial_src))

    virtualenv.run("python setup.py trial".format(setuptools_trial_src),
                   capture=True, cd=dummy_project_src)
