"""
Utility functions.
"""

import logging

from constants import LOG_DIRECTORY, LOG_FILENAME


def setup_logging():

    LOG_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    logging.basicConfig(

        filename=str(LOG_FILENAME),

        level=logging.INFO,

        format="%(asctime)s %(levelname)s %(message)s"

    )

    logging.info(
        "Logging started."
    )
