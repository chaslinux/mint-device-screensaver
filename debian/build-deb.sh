#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "Cleaning previous Debian builds..."

rm -rf debian/.debhelper
rm -rf debian/mint-device-screensaver
rm -f debian/files
rm -f debian/*.substvars
rm -f debian/*.debhelper


echo "Building Debian package..."

dpkg-buildpackage -us -uc


echo
echo "Build complete."
echo
echo "Package created:"
ls -lh ../mint-device-screensaver_*.deb
