#!/usr/bin/env python3
"""
main.py

Entry point for the Mint Device Screensaver.
"""

import sys

from application import Application
from version import VERSION, APP_NAME


def main():

    if "--version" in sys.argv:
        print(f"{APP_NAME} {VERSION}")
        return

    app = Application()

    app.run()


if __name__ == "__main__":

    main()
