#!/bin/sh

find "${DIRECTORY}" -name 'modules.json' -exec sh -c 'python3 /main.py "$1"' _ {} \;