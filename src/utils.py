"""
Utility functions.
"""

import logging

from constants import LOG_DIRECTORY, LOG_FILENAME



def setup_logging(debug=False):

    LOG_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )


    level = logging.DEBUG if debug else logging.INFO


    logging.basicConfig(

        filename=str(LOG_FILENAME),

        level=level,

        format="%(asctime)s %(levelname)s %(message)s"

    )


    if debug:

        logging.debug(
            "Debug logging enabled."
        )


    logging.info(
        "Logging started."
    )
