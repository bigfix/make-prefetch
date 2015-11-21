#!/bin/bash

set -e

# Clean up the background server when we finish
trap 'kill $(jobs -p)' EXIT

# Start a web server in the background
python2.7 server.py >/dev/null 2>&1 &

# Run the tests
python test-cases.py
