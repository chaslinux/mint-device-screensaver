"""
Utility functions.
"""

import logging

from constants import LOG_FILENAME


def setup_logging():

    logging.basicConfig(

        filename=LOG_FILENAME,

        level=logging.INFO,

        format="%(asctime)s %(levelname)s %(message)s"

    )

    logging.info("Logging started.")
