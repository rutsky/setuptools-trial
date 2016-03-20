import os

# Enable pytest-virtualenv debugging
os.environ["DEBUG"] = "x"

# TODO: add option or in other way allow developer to enable debug logging.
if True:
    import logging
    logging.basicConfig(level=logging.DEBUG)
